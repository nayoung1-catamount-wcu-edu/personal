# Load shiny
library(shiny)

# Load the color brewer package
library(RColorBrewer)

# Load the dplyr package
library(dplyr)

# Set working directory
setwd('C:/Users/natha/OneDrive/Desktop/personal/RScripts')

# Load Data
stocks <- read.csv("C:/Users/natha/OneDrive/Desktop/personal/Data/closing_stocks.csv")

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
        choices = c("MSFT", "AAPL", "GOOG", "AMZN"),
        selected = c("MSFT", "AAPL", "GOOG", "AMZN"))),
    mainPanel(
      plotOutput(
        outputId = "plot"))))

# Create a server
server <- function(input, output) {
  output$plot <- renderPlot({
    subset <- stocks %>%
      as.data.frame()
    plot(
      x = subset$Date, 
      y = subset$price, 
      col = colors[as.integer(subset$Rating)], 
      pch = 19,
      cex = 1.5,
      xlim = c(0, 100),
      ylim = c(0, 800),
      xlab = "Date",
      ylab = "Stock Price")
    legend(
      x = "topleft", 
      as.character(levels(stocks$index)), 
      col = colors[1:4], 
      pch = 19, 
      cex = 1.5)})
}

# Create a shiny app
shinyApp(
  ui = ui,
  server = server)

