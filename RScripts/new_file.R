# Set working directory
setwd('C:/Users/natha/OneDrive/Desktop/personal/RScripts')

if (!require("quantmod")) {
  install.packages("quantmod")
  library(quantmod)
}

start <- as.Date("2019-01-01")
end <- as.Date("2019-12-31")

getSymbols(c("MSFT","AAPL","GOOG"), src = 'yahoo', from = start, to = end)

stocks <- as.xts(data.frame(AAPL = AAPL[, "AAPL.Close"], MSFT = MSFT[, "MSFT.Close"], 
                            GOOG = GOOG[, "GOOG.Close"]))
head(stocks)

plot(as.zoo(stocks), screens = 1, lty = 1:3, xlab = "Date", ylab = "Price")
legend("right", c("AAPL", "MSFT", "GOOG"), lty = 1:3, cex = 0.5)
