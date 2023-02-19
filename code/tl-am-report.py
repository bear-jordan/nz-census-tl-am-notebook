import sentimentanalysis
import changedetection
import combineresults

def main():
    sentimentanalysis.run()
    changedetection.run()
    combineresults.run()

if __name__ == "__main__":
    main()