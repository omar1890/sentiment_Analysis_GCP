import argparse

from google.cloud import language_v1

"""Demonstrates how to make a simple call to the Natural Language API."""

import argparse

from google.cloud import language_v1

from google.oauth2 import service_account



def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print(
            "Sentence {} has a sentiment score of {}".format(index, sentence_sentiment)
        )

    print(
        "Overall Sentiment: score of {} with magnitude of {}".format(score, magnitude)
    )
    return 0




def analyze(movie_review_filename):
    """Run a sentiment analysis request on text within a passed filename."""
    credentials = service_account.Credentials.from_service_account_file("E:/ITI -AI pro/2022/GCP starting/bold-network-339320-62c4f5a8751a.json")

    client = language_v1.LanguageServiceClient(credentials=credentials)

    with open(movie_review_filename, "r") as review_file:
        # Instantiates a plain text document.
        content = review_file.read()

    document = language_v1.Document(
        content=content, type_=language_v1.Document.Type.PLAIN_TEXT
    )
    annotations = client.analyze_sentiment(request={"document": document})

    # Print the results
    print_result(annotations)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "movie_review_filename",
        help="The filename of the movie review you'd like to analyze.",
    )
    args = parser.parse_args()

    analyze(args.movie_review_filename)