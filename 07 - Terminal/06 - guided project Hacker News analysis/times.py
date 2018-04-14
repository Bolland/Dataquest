import dateutil
import read



def extracthour(timestamp):
    parsed = dateutil.parser.parse(timestamp)
    hour = parsed.hour
    #print(hour)
    return hour

    
if __name__ == "__main__":
    df = read.load_data()
    df['submission_hours'] = df['submission_time'].apply(extracthour)
    #print(df)
    print(df['submission_hours'].value_counts())    
