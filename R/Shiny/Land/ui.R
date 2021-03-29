library(shiny)
library(shinythemes)
library(plotly)
library(RODBC)
library(dplyr)
library(tidyverse)

con <- RODBC::odbcDriverConnect(
    "Driver={SQL Server Native Client 11.0};
    Server=localhost;
    Database=DataDashboard;
    Trusted_Connection=Yes"

)

# Get data
data <- RODBC::sqlQuery(con, "select * from vLand")

# Convert date column to datetime
data$Date <- as.Date(data$Date,
                     format = "%Y-%m-%d")

fluidPage(
    theme = shinytheme(theme = "flatly"),
    titlePanel(title = "Land Data"),
    sidebarLayout(
        sidebarPanel(
            htmlOutput("state_selector"),
            htmlOutput("county_selector"),
            htmlOutput("date_selector"),
        ),
        mainPanel(
            plotlyOutput(outputId = "land_plotly")
        )
    )
)
