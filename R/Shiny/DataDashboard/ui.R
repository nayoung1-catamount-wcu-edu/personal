library(shiny)
library(shinythemes)

fluidPage(
    theme = shinytheme(theme = "flatly"),
    titlePanel(title = "Demographics Data"),
    sidebarLayout(
        sidebarPanel(
            htmlOutput("state_selector"),
            htmlOutput("county_selector"),
            htmlOutput("date_selector"),
        ),
        mainPanel(
            plotlyOutput(outputId = "demographics_plotly")
        )
    )
)
