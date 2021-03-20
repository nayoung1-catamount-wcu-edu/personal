# Load libraries
library(shiny)

# plot cases by county
plot_covid <- function() {
  # Run the app
  shinyApp(ui = ui, server = server)
}