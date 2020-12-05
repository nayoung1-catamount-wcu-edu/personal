library(shinythemes)
library(tidyverse)

# read data
covid <-
  read.csv(file.path("Data/covid-19-data", "us-counties.csv"))



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
      htmlOutput("state_selector"),
      
      # user input county value eventually based on state value
      htmlOutput("county_selector"),
      
      # user input date range
      htmlOutput("date_selector")
    ),
    # print plot in main panel
    mainPanel(plotOutput(outputId = "covid_ggplot"), ),
    
  )
)