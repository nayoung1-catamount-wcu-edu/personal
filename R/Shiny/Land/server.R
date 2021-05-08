library(RODBC)
library(dplyr)
library(tidyverse)
library(ggplot2)
library(scales)

con <- RODBC::odbcDriverConnect(
  "Driver={SQL Server Native Client 11.0};
    Server=TITANIUM-BOOK;
    Database=DataDashboard;
    Trusted_Connection=Yes"
)

server <- function(input, output, session) {
  # Get data
  df <- RODBC::sqlQuery(con, "select * from vLand")

  # Split region column into County and State for filters
  df <- separate(df,
                   "Region Name",
                   c("County", "State"),
                   sep = ",")

  # rename columns
  df <- rename(df, Estimated_Value = "Estimated Value")
  df <- rename(df, Measure_Name = "Measure Name")

  # Order data by County ascending
  df <- df[order(df$County),]

  # Order data by State ascending
  df <- df[order(df$State),]

  # Convert date column to datetime
  df$Date <- as.Date(df$Date,
                       format = "%Y-%m-%d")

  # output State selector
  output$state_selector <- renderUI({
    selectInput(
      inputId = "state",
      label = "Choose a State:",
      choices = unique(df$State),
      selected = unique(df$State[1])
    )
  })

  # output County selector
  output$county_selector <- renderUI({
    available <- df[df$State == input$state, "county"]
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
                   start = "2000-01-01")
  })


  # plot data
  output$land_plotly <- renderPlotly({
    state_filter <- filter(df, State == input$state)
    county_filter <- filter(state_filter, County == input$county)
    p <- ggplot(data = county_filter,
                    aes(x = Date,
                    y = Estimated_Value,
                    group = Measure_Name)) +
      geom_line(aes(color = Measure_Name)) +
      geom_point(aes(color = Measure_Name)) +
      scale_x_date(limits = c(input$dates[1], input$dates[2]))
    ggplotly(p +
    ggtitle("Land Data"))
  })
}
