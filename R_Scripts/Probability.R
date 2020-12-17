## THIS PROGRAM CAN ONLY BE TRUSTED WHEN LB & UB NOT INF AND SD > 1 ##

#Solve normal distribution for 1 test
normalcdf <- function(x, mean, sd) {
  ans_greater_than_x <- 1 - pnorm(x, mean=mean, sd=sd)
  ans_less_than_x <- 1 - ans_greater_than_x
  cat("Answer if looking for greater than x:",
        round(ans_greater_than_x, digits=4))
  cat("\nAnswer if looking for less than x:",
      round(ans_less_than_x, digits=4))
}

#Solve normal distribution for >1 test
multi_normalcdf <- function(x,mean,sd,n) {
  ans_greater_than_x <- 1 - pnorm(x, mean=mean, sd=sd)
  ans_less_than_x <- 1 - ans_greater_than_x
  cat("Answer if looking for greater than x:",
      round(ans_greater_than_x, digits=4))
  cat("\nAnswer if looking for less than x:",
      round(ans_less_than_x, digits=4))
  }

#Solve Z scores
z_score <- function(x, sd) {
  mean <- mean(x)
  ans <- (x-mean) / sd
  print(round(ans, digits=4))
}