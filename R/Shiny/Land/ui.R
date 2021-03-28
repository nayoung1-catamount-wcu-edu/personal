library(shiny)
library(shinythemes)
library(plotly)

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
            plotlyOutput(outputId = "plotly")
        )
    )
)
