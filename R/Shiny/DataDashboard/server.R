library(shiny)
library(odbc)

server <- function(input, output, session) {
  # read data from database
  data <- dbConnect(odbc(),
                    Driver = "SQL Server Native Client 11.0",
                    Server = "localhost",
                    Database = "DataDashboard",
                    Trusted_Connection = "Yes")

  # split
  data

  output$state_selector <- renderUI({
    selectInput(
      inputId = "state",
      label = "Choose a State:"
      choices = unique(data)
    )
  })
}


