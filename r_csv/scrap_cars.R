library(rvest)
m <- matrix(unlist(strsplit(html_text(html_nodes(read_html("https://en.wikipedia.org/wiki/Comma-separated_values")
                                                       , ".wikitable"), trim=TRUE), "\n")),ncol=5,byrow=T)
colnames(m) <- m[1,]
write.csv(data.frame(m[-1,]), "/Users/levbarbash/LondonProg/Assignment2/cars.csv", row.names = FALSE)
