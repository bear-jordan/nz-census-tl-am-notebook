import sentimentanalysis
import changedetection
import combineresults

def main():
    sentimentanalysis.run()
    changedetection.run()
    combineresults.run()
    
    print("See results in ./result/to-check.csv")

if __name__ == "__main__":
    main()