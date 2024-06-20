import random
import json


def generate_test_cases(urls):
    """
    Generate test cases by applying metamorphic relations to a given list of URLs.

    Args:
        urls (list): A list of URLs.

    Returns:
        dict: A dictionary containing the original URL and the transformed URLs for each metamorphic relation.
            The dictionary has the following structure:
            {
                "Original": [original_url_1, original_url_2, ...],
                "MR1": [transformed_url_1, transformed_url_2, ...],
                "MR2": [transformed_url_1, transformed_url_2, ...],
                "MR3": [transformed_url_1, transformed_url_2, ...],
                "MR4": [transformed_url_1, transformed_url_2, ...],
                "MR5": [transformed_url_1, transformed_url_2, ...]
            }
    """
    test_cases = {"Original": [], "MR1": [], "MR2": [], "MR3": [], "MR4": [], "MR5": []}
    for url in urls:
        # Original URL
        test_cases["Original"].append(url)

        # MR1: URL Length Invariance
        if "?" in url:
            transformed_url_mr1 = url + "&extra=params"
        else:
            transformed_url_mr1 = url + "?extra=params"
        test_cases["MR1"].append(transformed_url_mr1)

        # MR2: HTTPS vs. HTTP
        if url.startswith("http://"):
            transformed_url_mr2 = url.replace("http://", "https://")
        elif url.startswith("https://"):
            transformed_url_mr2 = url.replace("https://", "http://")
        else:
            transformed_url_mr2 = url
        test_cases["MR2"].append(transformed_url_mr2)

        # MR3: Subdomain Addition
        parts = url.split("//")
        if len(parts) > 1:
            base = parts[1]
            subdomain = "safe."
            transformed_url_mr3 = parts[0] + "//" + subdomain + base
        else:
            transformed_url_mr3 = "http://safe." + url
        test_cases["MR3"].append(transformed_url_mr3)

        # MR4: Parameter Shuffling
        if "?" in url:
            base_url, params = url.split("?", 1)
            param_list = params.split("&")
            if len(param_list) > 1:
                shuffled_params = "&".join(sorted(param_list))
                transformed_url_mr4 = base_url + "?" + shuffled_params
                test_cases["MR4"].append(transformed_url_mr4)
            else:
                test_cases["MR4"].append(url)
        else:
            test_cases["MR4"].append(url)

        # MR5: Case Variation in Path
        if "://" in url:
            scheme, path = url.split("://", 1)
            transformed_url_mr5 = scheme + "://" + path.upper()
            test_cases["MR5"].append(transformed_url_mr5)
        else:
            test_cases["MR5"].append(url.upper())

    return test_cases


def main():
    """
    Main function to generate test URLs and write them to a file.
    """
    input_file = "URL dataset.csv"
    output_file = "mutamorphic_urls.txt"
    sample_size = 5000

    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        urls = []
        for line in infile:
            url = line.split(",")[0].strip()
            if url:
                urls.append(url)
            if len(urls) % 1000 == 0:
                print(f"Read {len(urls)} URLs from the input file.", end="\r")

        sampled_urls = random.sample(urls, sample_size)

        test_cases = generate_test_cases(sampled_urls)
        json.dump(test_cases, outfile, indent=4)

    print(f"Test URLs generated and written to {output_file}.")


if __name__ == "__main__":
    main()
