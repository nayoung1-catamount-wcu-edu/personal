landslides <- function(target, train_size) {

   library(dplyr)
   library(fastDummies)

   # read data and strip whitespace from column names
   data <- read.csv("https://data.nasa.gov/api/views/dd9e-wu2v/rows.csv?accessType=DOWNLOAD", strip.white=TRUE)
   
   # get dummies for target column and join dummies to new dataframe
   data <- dummy_cols(data, select_columns = 'landslide_category', remove_selected_columns = TRUE)
   df <- data.frame(data)

   # drop character and numeric dtypes
   df <- df[, !sapply(df, is.character)]

   # remove unwanted columns
   df <- select(df, -c("event_id", "event_time", "longitude", "latitude", "event_import_id", "admin_division_population", "gazeteer_distance", "landslide_category_"))

   df <- na.omit(df)

   split_train_test(d=df, outcome=target, percent_train=train_size, seed=1)
}