library(shiny)
library(odbc)

function(input, output, session) {
  data <- dbConnect(odbc(),
                    Driver = "SQL Server Native Client 11.0",
                    Server = "localhost",
                    Database = "DataDashboard",
                    Trusted_Connection = "Yes")
}
