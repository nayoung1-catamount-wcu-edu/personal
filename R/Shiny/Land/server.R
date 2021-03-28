library(RODBC)
library(dplyr)
library(tidyverse)
library(ggplot2)

con <- RODBC::odbcDriverConnect(
  "Driver={SQL Server Native Client 11.0};
    Server=localhost;
    Database=DataDashboard;
    Trusted_Connection=Yes"
)

server <- function(input, output, session) {
  # Get data
  data <- RODBC::sqlQuery(con, "select * from vLand")

  # Split region column into County and State for filters
  data <- separate(data,
                   "Region Name",
                   c("County", "State"),
                   sep = ",")

  # Order data by County ascending
  data <- data[order(data$County), ]

  # Order data by State ascending
  data <- data[order(data$State), ]

  # Convert date column to datetime
  data$Date <- as.Date(data$Date,
                       format = "%Y-%m-%d")

  # output State selector
  output$state_selector <- renderUI({
    selectInput(
      inputId = "state",
      label = "Choose a State:",

      choices = unique(data$state),
      selected = unique(data$state[1])
    )
  })

  # output County selector
  output$county_selector <- renderUI({
    available <- data[data$State == input$state, "county"]
    selectInput(
      inputId = "county",
      label = "Choose a County/Munisipality:",
      choices = unique(available),
      selected = unique(available[1])
    )
  })

  # output range of dates
  output$date_selector <- renderUI({
    dateRangeInput(inputId = "dates",
                   label = "Select a Range of Dates",
                   start = "2020-01-01")
  })

  # plot data
  output$land_plotly <- renderPlotly({
    state_filter <- filter(data, state == input$state)
    county_filter <- filter(data, county == input$county)
    p <- ggplot(data = county_filter,
                aes(x = "Date",
                    y = "Estimated Value",
                    group = "Measure Name")) +
      geom_line(aes(color = "Measure Name")) +
      geom_point(aes(color = "Measure_Name")) +
      scale_x_date(limits = c(input$dates[1], input$dates[2]))
    ggplotly(p +
               ggtitle("Land Data"))
  })
}
