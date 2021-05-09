library(shinythemes)
library(tidyverse)
library(plotly)

# read data
covid <-
  read.csv(file.path("Data/covid-19-data", "us-counties.csv"))

# convert date column to date dtype
covid$date <- as.Date(covid$date, format = "%Y-%m-%d")

# build ui
fluidPage(
# set theme
  theme = shinytheme(theme = "flatly"),
# set title
  titlePanel(title = "COVID Cases and Deaths"),
# create sidebar
  sidebarLayout(
    sidebarPanel(
# user input state value
      htmlOutput("state_selector"),
# user input county value eventually based on state value
      htmlOutput("county_selector"),
# user input date range
      htmlOutput("date_selector")
    ),
# print plot in main panel
    mainPanel(
      plotlyOutput(outputId = "covid_plotly"),
      p("This project has become too large for ShinyApps.io and thus will no longer be updated, though data will still be collected."),
      p("COVID Cases and Deaths updates every day around 5pm EST."),
      p("Source: ",
        a("NY Times",
          href = "https://github.com/nytimes/covid-19-data")),
    ),
  )
)