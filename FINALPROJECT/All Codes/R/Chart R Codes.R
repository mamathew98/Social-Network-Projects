
## For social network final projects ##
## Team members : Amirhossein Mehrvarz - Mohammad Naseri - Hooman Moshirizadeh

# ggplot2 library for plotting 

library('ggplot2')

################# 

data = read.csv(file.choose())

ggplot(data) + 
  geom_bar(aes(x = data$Degree , y = reorder(data$Label,data$Degree)), stat = 'identity',fill = '#425f8f') +
  theme(axis.text.x=element_text(angle=90,hjust=1,vjust=0.5)) +
  labs(title = "Most Repeated Words", x = "Counts", y = "Words")+
  theme(plot.title = element_text(hjust = 0.5))


################# 

data = read.csv(file.choose())

ggplot(data) + 
  geom_bar(aes(x=data$closnesscentrality,y=reorder(data$Label,data$closnesscentrality)), stat = 'identity',fill = '#425f8f') +
  theme(axis.text.x=element_text(angle=90,hjust=1,vjust=0.5)) +
  labs(title = "Top Words In Closeness Centrality", x = "Closeness", y = "Words")+
  theme(plot.title = element_text(hjust = 0.5))


#################

data = read.csv(file.choose())
View(data)

library('ggplot2')

ggplot(data) + 
  geom_bar(aes(x=data$betweenesscentrality,y=reorder(data$Label,data$betweenesscentrality)), stat = 'identity',fill = '#425f8f') +
  theme(axis.text.x=element_text(angle=90,hjust=1,vjust=0.5)) +
  labs(title = "Top 20 words In Betweeness Centrality", x = "Betweeness", y = "Words")+
  theme(plot.title = element_text(hjust = 0.5)) 


#################



data = read.csv(file.choose())
View(data)


library('ggplot2')

ggplot(data) + 
  geom_bar(aes(x=data$clustering,y=reorder(data$Label,data$clustering)), stat = 'identity',fill = '#425f8f') +
  theme(axis.text.x=element_text(angle=90,hjust=1,vjust=0.5)) +
  labs(title = "Top 30 words Clustering Coefficient", x = "Clustering Coefficient", y = "Words")+
  theme(plot.title = element_text(hjust = 0.5)) 


#################



data = read.csv(file.choose())
View(data)


library('ggplot2')

ggplot(data) + 
  geom_bar(aes(x=data$eigencentrality,y=reorder(data$Label,data$eigencentrality)), stat = 'identity',fill = '#425f8f') +
  theme(axis.text.x=element_text(angle=90,hjust=1,vjust=0.5)) +
  labs(title = "Top 30 words Eigenvector Centrality", x = "Eigenvector Centrality", y = "Words")+
  theme(plot.title = element_text(hjust = 0.5)) 


#################


data = read.csv(file.choose())
View(data)


library('ggplot2')

ggplot(data) + 
  geom_bar(aes(x=data$pageranks,y=reorder(data$Label,data$pageranks)), stat = 'identity',fill = '#425f8f') +
  theme(axis.text.x=element_text(angle=90,hjust=1,vjust=0.5)) +
  labs(title = "Top 20 words In PageRank Centrality", x = "PageRank Centrality", y = "Words")+
  theme(plot.title = element_text(hjust = 0.5)) 


#################


data = read.csv(file.choose())
View(data)


library('ggplot2')

ggplot(data) + 
  geom_bar(aes(x=data$Authority,y=reorder(data$Label,data$Authority)), stat = 'identity',fill = '#425f8f') +
  theme(axis.text.x=element_text(angle=90,hjust=1,vjust=0.5)) +
  labs(title = "Top 30 words In Hub & Authority Centrality", x = "Hub & Authority Centrality", y = "Words")+
  theme(plot.title = element_text(hjust = 0.5)) 



#################


data = read.csv(file.choose())
View(data)


library('ggplot2')

ggplot(data) + 
  geom_bar(aes(x=data$Authority,y=reorder(data$Label,data$Authority)), stat = 'identity',fill = '#425f8f') +
  theme(axis.text.x=element_text(angle=90,hjust=1,vjust=0.5)) +
  labs(title = "Top 30 words In Hub & Authority Centrality", x = "Hub & Authority Centrality", y = "Words")+
  theme(plot.title = element_text(hjust = 0.5)) 
















       