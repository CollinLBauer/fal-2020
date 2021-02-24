# Collin Bauer
# MATH-250 Project

# I decided I would try to run R from the command line instead of using Rstudio.
# This causes two issues with installing packages:
#  1. a repo link is required
#  2. On Windows, it needs to be run as an administrator for write access
# As long as the package is already installed, that line may be left commented out.

#install.packages("readxl", repos = "http://cran.us.r-project.org")

library("readxl")
data=read_xlsx("Mount_Pleasant_Real_Estate_Data.xlsx")
data_c = subset(data, Subdivision == "Carolina Park")
data_d = subset(data, Subdivision == "Dunes West")
data_p = subset(data, Subdivision == "Park West")

summary(data)

# Use technology to make a histogram for List Price and describe the distribution.
hist(data$`List Price`)

# For the variable List Price, calculate the sample mean, the sample standard
#  deviation, and the sample size for the three di↵erent subdivisions.
# Put the calculations in a table and round to the nearest dollar for the
#  sample standard deviation and the mean.

# Mean for each subdivision
data_mean = mean(data$`List Price`)
data_c_mean = mean(data_c$`List Price`)
data_d_mean = mean(data_d$`List Price`)
data_p_mean = mean(data_p$`List Price`)
cat("\nMeans...\n")
aggregate(data[ ,2], list(data$`Subdivision`), mean)
cat(paste("Population:\t", round(data_mean, digits=2), "\n"))

# Sample standard deviation for each subdivision
data_sd = sd(data$`List Price`)
data_c_sd = sd(data_c$`List Price`)
data_d_sd = sd(data_d$`List Price`)
data_p_sd = sd(data_p$`List Price`)
cat("\nStandard deviations...\n")
aggregate(data[ ,2], list(data$`Subdivision`), sd)
cat(paste("Population:\t", round(data_sd, digits=2), "\n"))

# Length of each subdivision
data_len = length(data$`List Price`)
data_c_len = length(data_c$`List Price`)
data_d_len = length(data_d$`List Price`)
data_p_len = length(data_p$`List Price`)
cat("\nLengths...\n")
aggregate(data[ ,2], list(data$`Subdivision`), length)
cat(paste("Population:\t", data_len, "\n"))

# Create a scatterplot of List Price vs. Squarefootage
plot(data$`Square Footage`, data$`List Price`, main="Price per Foot (all subdivisions)", xlim = c(1,8000), ylim= c(1,2000000))

plot(data_c$`Square Footage`, data_c$`List Price`, main="Price per Foot (Carolina Park)", xlim = c(1,8000), ylim= c(1,2000000))
plot(data_d$`Square Footage`, data_d$`List Price`, main="Price per Foot (Dunes West)", xlim = c(1,8000), ylim= c(1,2000000))
plot(data_p$`Square Footage`, data_p$`List Price`, main="Price per Foot (Park West)", xlim = c(1,8000), ylim= c(1,2000000))


# z interval or t interval?
cat("\nSince our data set is a large population that we have full informaiton about, a Z-score is appropriate.\n\n")
#scale(data$`List Price`)

cat("Critical values...\n")
cat(paste("Population:    ", round(qnorm(0.5, data_mean, data_sd), digits=2), "\n"))
cat(paste("Carolina Park: ", round(qnorm(0.5, data_c_mean, data_c_sd), digits=2), "\n"))
cat(paste("Dunes west:    ", round(qnorm(0.5, data_d_mean, data_d_sd), digits=2), "\n"))
cat(paste("Park West:     ", round(qnorm(0.5, data_p_mean, data_p_sd), digits=2), "\n"))

cat("\nA list price of $520,000 is reasonable for Carolina Park.\n")
cat("A list price of $670,000 is reasonable for Dunes West.\n")
cat("A list price of $568,000 is barely acceptable for Park West, but not reasonable for Carolina Park.\n")