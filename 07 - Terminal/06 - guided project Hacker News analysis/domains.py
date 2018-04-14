import read
df = read.load_data()

if __name__ == "__main__":
   domains = df['url'].value_counts()
   #print(domains.head(100))
   #for name, row in domains.items():
      print("{0}: {1}".format(name, row))
