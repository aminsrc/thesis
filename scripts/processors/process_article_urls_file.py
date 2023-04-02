strings_to_remove = ["how-to-find-rockstar-api-product-manager-your-public-apis",
                    "how-to-implement-deep-linking-ios",
                    "how-to-get-started-twitters-fabric",
                    "how-to-develop-android-wear-application",
                    "google-finalizes-android-n-apis-and-sdk",
                    "hitch-aims-to-improve-engagement-between-api-providers-and-developers",
                    "getting-started-locationkit-ios-and-android",
                    "google-finalizes-android-n-apis-and-sdk",
                    "getting-started-locationkit-ios-and-android",
                    "10-lessons-to-learn-10-years-aws"]

with open('article_urls.txt', 'r') as oldfile, open('processed_article_urls.txt', 'w') as newfile:
    for line in oldfile:
        if not any(bad_string in line for bad_string in strings_to_remove):
            newfile.write(line)
