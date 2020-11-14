library(reshape2)
library(ggplot2)
library(tidyverse)
library(ggdark)

# Define server logic
server <- function(input, output, session) {
  # read data
  covid <-
    read.csv(file.path("../Data/covid-19-data", "us-counties.csv"))
  
  # melt data
  covid_melt <-
    melt(covid, id = c("date", "county", "state", "fips"))
  
  # convert date column to date dtype
  covid_melt$date <- as.Date(covid_melt$date, format = "%Y-%m-%d")
  
  # output range of dates
  output$dates <- renderPrint({
    input$dates
  })
  
  # plot cases and deaths by selected state and eventually county in selected state
  output$covid <- renderPlot({
    county_filter <- filter(covid_melt, county == input$county)
    ggplot(data = county_filter, aes(x = date,
                                     y = value,
                                     fill = variable)) +
      geom_bar(stat = "identity") +
      scale_x_date(limits = c(input$dates[1], input$dates[2])) +
      geom_text(aes(label = value, vjust = -1)) +
      dark_theme_minimal()
  })
}