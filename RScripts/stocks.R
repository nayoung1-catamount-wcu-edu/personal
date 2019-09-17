# Load shiny
library(shiny)

# Load the color brewer package
library(RColorBrewer)

# Load the dplyr package
library(dplyr)

# Set working directory
setwd('C:/Users/natha/OneDrive/Desktop/personal/RScripts')

# Load Data
stocks <- read.csv("C:/Users/natha/OneDrive/Desktop/personal/Data/closing_stocks_unpivoted.csv")

colors <- brewer.pal(4, "Set3")

# Create a user interface
ui <- fluidPage(
  titlePanel("Interactive Stock Data"),
  sidebarLayout(
    sidebarPanel(
      sliderInput(
        inputId = "year",
        label = "Year",
        min = 2000,
        max = 2020,
        value = c(2000, 2021),
        sep = ""),
      checkboxGroupInput(
        inputId = "stockID",
        label = "Stock ID",
        choices = c("MSFT", "AAPL", "GOOG", "AMZN", "IBM"),
        selected = c("MSFT", "AAPL", "GOOG", "AMZN", "IBM")),
    mainPanel(
      plotOutput(
        outputId = "plot"))))

# Create a server
server <- function(input, output) {
  output$plot <- renderPlot({
    subset <- stocks %>%
      as.data.frame()
   })
}

# Create a shiny app
shinyApp(
  ui = ui,
  server = server)
