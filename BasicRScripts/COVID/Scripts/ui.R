library(shinythemes)
library(tidyverse)

# read data
covid <-
  read.csv(file.path("../Data/covid-19-data", "us-counties.csv"))

# order county values ascending
covid <- covid[order(covid$county), ]

# order state values ascending
covid <- covid[order(covid$state), ]

# convert date column to date dtype
covid$date <- as.Date(covid$date, format = "%Y-%m-%d")

# build ui
fluidPage(
  # set theme
  theme = shinytheme(theme = "cyborg"),
  
  # set title
  titlePanel(title = "COVID Case and Deaths"),
  
  # create sidebar
  sidebarLayout(
    sidebarPanel(
      # user input state value
      selectInput(
        inputId = "state",
        label = "Choose a State",
        choices = unique(covid$state),
        selected = ""
      ),
      # user input county value eventually based on state value
      selectInput(
        inputId = "county",
        label = "Choose a County",
        choices = unique(covid$county),
        selected = ""
      ),
      # user input date range
      dateRangeInput(
        inputId = "dates",
        label = "Select a Range of Dates",
        start = "2020-11-01"
      ),
      
      # action to turn labels on
      actionButton(inputId = "show_labels", label = "Show Labels"),
      
      # action to turn labels off
      actionButton(inputId = "hide_labels", label = "Hide Labels"),
    ),
    # print plot in main panel
    mainPanel(plotOutput(outputId = "covid"), ),
  )
)