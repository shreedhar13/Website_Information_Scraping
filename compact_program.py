import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

"""
    Scrape a given website for various details such as social media links, 
    tech stack, meta title and description, payment gateways, language, 
    and category. Includes retry logic for handling request failures.

    Parameters:
    url (str): The URL of the website to scrape.
    retries (int): The number of times to retry the request in case of failure. Default is 2.
    timeout (int): The time (in seconds) to wait for a response before timing out. Default is 2.

    Returns:
    dict: A dictionary containing the scraped information.

"""


def scrape_website(url, retries=2, timeout=2):
    #Initializing Header for request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    for attempt in range(retries):
        try:
            # Send GET request to the URL
            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()  # Raise an exception for bad response status

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Dictionary of social media platforms and their respective domains
            social_media_platforms = {
                        'Facebook': ['facebook.com'],
                        'Twitter': ['twitter.com'],
                        'Instagram': ['instagram.com'],
                        'LinkedIn': ['linkedin.com'],
                        'YouTube': ['youtube.com'],
                        'Pinterest': ['pinterest.com'],
                        'TikTok': ['tiktok.com'],
                        'Snapchat': ['snapchat.com'],
                        'Reddit': ['reddit.com'],
                        'Tumblr': ['tumblr.com'],
                        'WhatsApp': ['whatsapp.com'],
                        'WeChat': ['wechat.com'],
                        'Telegram': ['telegram.org'],
                        'Discord': ['discord.com'],
                        'Clubhouse': ['joinclubhouse.com'],
                        'Quora': ['quora.com'],
                        'Medium': ['medium.com'],
                        'Flickr': ['flickr.com'],
                        'Vimeo': ['vimeo.com'],
                        'Twitch': ['twitch.tv'],
                        'Vine': ['vine.co'],
                        'Myspace': ['myspace.com'],
                        'VKontakte (VK)': ['vk.com'],
                        'Sina Weibo': ['weibo.com'],
                        'XING': ['xing.com'],
                        'Yubo': ['yubo.live'],
                        'Meetup': ['meetup.com'],
                        'Nextdoor': ['nextdoor.com'],
                        'Gab': ['gab.com'],
                        'Parler': ['parler.com'],
                        }
                        
    #1) Extract social media links
            social_media_links = {}
            links = soup.find_all('a', href=True)
            for link in links:
                href = link['href']
                for platform, domains in social_media_platforms.items():
                    if any(domain in href for domain in domains):
                        social_media_links[platform] = href


    #2) Meta Title
            meta_title = soup.find('title').text.strip() if soup.find('title') else 'N/A'
            

    #3) Meta Description
            meta_description = soup.find('meta', attrs={'name': 'description'})
            meta_description = meta_description['content'].strip() if meta_description else 'N/A'


    #4) Tech Stack
            tech_stack = []
            scripts = soup.find_all('script', src=True)
            links = soup.find_all('link', href=True)
            
            for script in scripts:
                src = script.get('src', '').lower()
                if 'react' in src:
                    tech_stack.append('React.js')
                if 'angular' in src:
                    tech_stack.append('Angular')
                if 'vue' in src:
                    tech_stack.append('Vue.js')
                if 'jquery' in src:
                    tech_stack.append('jQuery')
                if 'backbone' in src:
                    tech_stack.append('Backbone.js')
                if 'ember' in src:
                    tech_stack.append('Ember.js')
                if 'svelte' in src:
                    tech_stack.append('Svelte')
                if 'polymer' in src:
                    tech_stack.append('Polymer')
                if 'alpine' in src:
                    tech_stack.append('Alpine.js')
                if 'stimulus' in src:
                    tech_stack.append('Stimulus.js')
                if 'riot' in src:
                    tech_stack.append('Riot.js')
                # Add more frontend frameworks/libraries as needed

                # Check links for CSS frameworks
                for link in links:
                    href = link.get('href', '').lower()
                    if 'bootstrap' in href:
                        tech_stack.append('Bootstrap')
                    if 'foundation' in href:
                        tech_stack.append('Foundation')
                    if 'materialize' in href:
                        tech_stack.append('Materialize CSS')
                    if 'bulma' in href:
                        tech_stack.append('Bulma')
                    if 'tailwind' in href:
                        tech_stack.append('Tailwind CSS')
                    if 'sass' in href or 'scss' in href:
                        tech_stack.append('Sass')
                    if 'less' in href:
                        tech_stack.append('Less')
                    if 'stylus' in href:
                        tech_stack.append('Stylus')
                    # Add more CSS frameworks/preprocessors as needed

                # Check for MVC frameworks
                if 'django' in tech_stack:
                    tech_stack.append('Django (MVC)')
                if 'rails' in tech_stack or 'ruby on rails' in tech_stack:
                    tech_stack.append('Ruby on Rails (MVC)')
                if 'spring boot' in tech_stack:
                    tech_stack.append('Spring Boot (MVC)')
                if 'express' in tech_stack or 'node.js' in tech_stack:
                    tech_stack.append('Express.js (MVC)')
                # Add more MVC frameworks as needed

                # Check for CMS platforms
                if 'wordpress' in tech_stack:
                    tech_stack.append('WordPress (CMS)')
                if 'drupal' in tech_stack:
                    tech_stack.append('Drupal (CMS)')
                if 'joomla' in tech_stack:
                    tech_stack.append('Joomla (CMS)')
                # Add more CMS platforms as needed

                # Check for databases
                if 'mysql' in tech_stack:
                    tech_stack.append('MySQL')
                if 'postgresql' in tech_stack or 'postgres' in tech_stack:
                    tech_stack.append('PostgreSQL')
                if 'sqlite' in tech_stack:
                    tech_stack.append('SQLite')
                if 'mongodb' in tech_stack:
                    tech_stack.append('MongoDB')
                if 'redis' in tech_stack:
                    tech_stack.append('Redis')
                # Add more databases as needed

                # Check for programming languages
                if 'javascript' in tech_stack:
                    tech_stack.append('JavaScript')
                if 'python' in tech_stack:
                    tech_stack.append('Python')
                if 'java' in tech_stack:
                    tech_stack.append('Java')
                if 'c#' in tech_stack:
                    tech_stack.append('C#')
                if 'php' in tech_stack:
                    tech_stack.append('PHP')
                if 'ruby' in tech_stack:
                    tech_stack.append('Ruby')
                if 'go' in tech_stack:
                    tech_stack.append('Go')
                if 'swift' in tech_stack:
                    tech_stack.append('Swift')
                if 'kotlin' in tech_stack:
                    tech_stack.append('Kotlin')
                if 'typescript' in tech_stack:
                    tech_stack.append('TypeScript')
                # Add more programming languages as needed
            
            for link in links:
                href = link['href'].lower()
                if 'bootstrap' in href:
                    tech_stack.append('Bootstrap')
                if 'foundation' in href:
                    tech_stack.append('Foundation')
                # Add more CSS frameworks as needed
            
            tech_stack = ', '.join(set(tech_stack))
            


    #5) Payement Gateways
            payment_gateways = []
            html_content = str(soup)

            # Global Payment Gateways
            if re.search(r'paypal', html_content, re.IGNORECASE):
                payment_gateways.append('PayPal')
            if re.search(r'stripe', html_content, re.IGNORECASE):
                payment_gateways.append('Stripe')
            if re.search(r'square', html_content, re.IGNORECASE):
                payment_gateways.append('Square')
            if re.search(r'authorize\.net', html_content, re.IGNORECASE):
                payment_gateways.append('Authorize.Net')
            if re.search(r'2checkout|verifone', html_content, re.IGNORECASE):
                payment_gateways.append('2Checkout (Verifone)')
            if re.search(r'braintree', html_content, re.IGNORECASE):
                payment_gateways.append('Braintree')
            if re.search(r'amazon pay', html_content, re.IGNORECASE):
                payment_gateways.append('Amazon Pay')
            if re.search(r'google pay', html_content, re.IGNORECASE):
                payment_gateways.append('Google Pay')
            if re.search(r'apple pay', html_content, re.IGNORECASE):
                payment_gateways.append('Apple Pay')

            # Regional Payment Gateways
            if re.search(r'razorpay', html_content, re.IGNORECASE):
                payment_gateways.append('Razorpay')
            if re.search(r'payu', html_content, re.IGNORECASE):
                payment_gateways.append('PayU')
            if re.search(r'paytm', html_content, re.IGNORECASE):
                payment_gateways.append('Paytm')
            if re.search(r'phonepe', html_content, re.IGNORECASE):
                payment_gateways.append('PhonePe')
            if re.search(r'ccavenue', html_content, re.IGNORECASE):
                payment_gateways.append('CCAvenue')
            if re.search(r'instamojo', html_content, re.IGNORECASE):
                payment_gateways.append('Instamojo')
            if re.search(r'mollie', html_content, re.IGNORECASE):
                payment_gateways.append('Mollie')
            if re.search(r'klarna', html_content, re.IGNORECASE):
                payment_gateways.append('Klarna')
            if re.search(r'adyen', html_content, re.IGNORECASE):
                payment_gateways.append('Adyen')
            if re.search(r'alipay', html_content, re.IGNORECASE):
                payment_gateways.append('Alipay')
            if re.search(r'wechat pay', html_content, re.IGNORECASE):
                payment_gateways.append('WeChat Pay')
            if re.search(r'bluesnap', html_content, re.IGNORECASE):
                payment_gateways.append('BlueSnap')
            if re.search(r'worldpay', html_content, re.IGNORECASE):
                payment_gateways.append('Worldpay')
            if re.search(r'payoneer', html_content, re.IGNORECASE):
                payment_gateways.append('Payoneer')
            if re.search(r'bitpay', html_content, re.IGNORECASE):
                payment_gateways.append('BitPay')
            if re.search(r'skrill', html_content, re.IGNORECASE):
                payment_gateways.append('Skrill')
            if re.search(r'neteller', html_content, re.IGNORECASE):
                payment_gateways.append('Neteller')

            # Additional Payment Gateways
            if re.search(r'dwolla', html_content, re.IGNORECASE):
                payment_gateways.append('Dwolla')
            if re.search(r'venmo', html_content, re.IGNORECASE):
                payment_gateways.append('Venmo')
            if re.search(r'sezzle', html_content, re.IGNORECASE):
                payment_gateways.append('Sezzle')
            if re.search(r'afterpay', html_content, re.IGNORECASE):
                payment_gateways.append('Afterpay')
            if re.search(r'zelle', html_content, re.IGNORECASE):
                payment_gateways.append('Zelle')
            if re.search(r'payline', html_content, re.IGNORECASE):
                payment_gateways.append('Payline')
            if re.search(r'verifone', html_content, re.IGNORECASE):
                payment_gateways.append('Verifone')
            if re.search(r'eway', html_content, re.IGNORECASE):
                payment_gateways.append('Eway')
            if re.search(r'gocardless', html_content, re.IGNORECASE):
                payment_gateways.append('GoCardless')
            if re.search(r'payza', html_content, re.IGNORECASE):
                payment_gateways.append('Payza')
            if re.search(r'paysera', html_content, re.IGNORECASE):
                payment_gateways.append('Paysera')
            if re.search(r'paymill', html_content, re.IGNORECASE):
                payment_gateways.append('Paymill')

            payment_gateways = ', '.join(payment_gateways)



    #6) Language
            language = soup.find('html').get('lang') if soup.find('html') else 'N/A'


    #7) Categories
            categories = {
                    'E-commerce': ['shop', 'store', 'product', 'ecommerce', 'shopping', 'buy', 'sell', 'retail', 'marketplace', 
                                'online shop', 'storefront', 'online store', 'shopping cart', 'checkout', 
                                'e-commerce platform', 'online marketplace', 'digital storefront', 'buy online'],
                    'News and Media': ['news', 'magazine', 'blog', 'press', 'journal', 'newspaper', 'media', 'editorial', 
                                    'headline', 'current events', 'journalism', 'publication', 'breaking news', 
                                    'media outlet', 'online magazine', 'news updates', 'news commentary'],
                    'Corporate': ['business', 'corporate', 'company', 'enterprise', 'organization', 
                                'business solutions', 'business services', 'global business', 'industry', 
                                'corporate website', 'business development', 'company profile', 'enterprise solutions'],
                    'Technology': ['saas', 'tech', 'software', 'hardware', 'technology', 'digital', 'IT', 'innovation', 
                                'internet', 'software development', 'tech news', 'digital transformation', 'cloud computing', 
                                'tech solutions', 'digital services', 'IT infrastructure', 'tech support'],
                    'Educational': ['course', 'learning', 'university', 'education', 'study', 'classroom', 'academic', 
                                    'online courses', 'distance learning', 'educational resources', 'academic programs', 
                                    'educational platform', 'learning management system', 'online education', 'academic institution'],
                    'Non-Profit and Government': ['nonprofit', 'ngo', 'government', 'charity', 'foundation', 'public sector', 
                                                'social services', 'community support', 'public policy', 'humanitarian', 
                                                'government agency', 'nonprofit organization', 'social impact', 'charitable foundation'],
                    'Entertainment': ['entertainment', 'gaming', 'music', 'movie', 'film', 'video', 'celebrity', 
                                    'entertainment news', 'pop culture', 'streaming', 'celebrity news', 'film reviews', 
                                    'entertainment industry', 'music streaming', 'movie reviews', 'gaming community'],
                    'Health and Fitness': ['health', 'fitness', 'medical', 'wellness', 'nutrition', 'exercise', 'healthcare', 
                                        'healthy living', 'medical advice', 'fitness tips', 'nutrition guide', 'mental health', 
                                        'health services', 'wellness programs', 'medical treatments', 'nutrition counseling'],
                    'Travel and Hospitality': ['travel', 'hotel', 'booking', 'vacation', 'tourism', 'resort', 'destination', 
                                            'travel guide', 'hotel booking', 'vacation rentals', 'tourist attractions', 
                                            'hospitality industry', 'travel agency', 'resort accommodations', 'tourism services'],
                    'Food and Beverage': ['restaurant', 'recipe', 'food', 'eatery', 'cooking', 'cuisine', 'beverage', 
                                        'recipes', 'culinary', 'foodie', 'dining', 'food reviews', 
                                        'restaurant reviews', 'culinary experiences', 'food delivery', 'beverage services'],
                    'Real Estate': ['realestate', 'property', 'realty', 'housing', 'apartment', 'home', 'estate', 
                                    'real estate listings', 'property management', 'housing market', 'real estate services', 
                                    'property investments', 'housing rentals', 'real estate agents', 'commercial property'],
                    'Personal': ['personal', 'portfolio', 'resume', 'cv', 'profile', 'bio', 'personal website', 
                                'online portfolio', 'personal branding', 'resume builder', 'professional profile', 
                                'personal blog', 'digital resume', 'career portfolio', 'online identity'],
                    'Community and Forums': ['community', 'forum', 'social', 'network', 'discussion', 'group', 'community site', 
                                            'online community', 'discussion forum', 'social network', 'community platform', 
                                            'forum discussion', 'social engagement', 'community networking', 'group interactions'],
                    'Financial Services': ['bank', 'insurance', 'investment', 'finance', 'financial', 'money', 'wealth', 
                                        'financial planning', 'banking services', 'investment management', 'insurance coverage', 
                                        'financial advice', 'wealth management', 'investment banking', 'insurance solutions'],
                    'Legal Services': ['law', 'legal', 'attorney', 'lawyer', 'legal services', 'legal advice', 
                                    'law firm', 'legal counsel', 'legal representation', 'court cases', 
                                    'legal assistance', 'legal counsel', 'litigation services', 'legal solutions'],
                    'Fashion and Beauty': ['fashion', 'beauty', 'style', 'cosmetics', 'makeup', 'clothing', 'fashionista', 
                                        'fashion trends', 'beauty tips', 'style guides', 'cosmetic products', 
                                        'fashion industry', 'beauty industry', 'style advice', 'cosmetic enhancements'],
                    'Automotive': ['car', 'automotive', 'vehicle', 'truck', 'auto', 'motorcycle', 'car dealer', 
                                'automobile', 'vehicle sales', 'car reviews', 'auto repair', 
                                'automotive industry', 'vehicle services', 'auto parts', 'vehicle maintenance'],
                    'Others': ['classifieds', 'jobs', 'event', 'listing', 'classified', 'career', 'event management', 
                            'classified ads', 'job search', 'job listings', 'event planning', 
                            'community events', 'job opportunities', 'event coordination', 'classified listings']
}

            category = 'Other'
            url_lower = url.lower()

            for cat, keywords in categories.items():
                if any(keyword in url_lower for keyword in keywords):
                    category = cat
                    break
            

    #returning the Info of each website as Dictionary
            return {
                'URL': url,
                'Social Media Links': social_media_links,
                'Tech Stack': tech_stack,
                'Meta Title': meta_title,
                'Meta Description': meta_description,
                'Payment Gateways': payment_gateways,
                'Language': language,
                'Category': category
            }
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt+1}/{retries} failed for {url}: {e}")
            if attempt < retries - 1:
                print("Retrying...")
                time.sleep(2)  # Wait 2 seconds before retrying
                continue
            else:
                print(f"Failed to scrape {url} after {retries} attempts.")
                return None



#Main Function Starts From Here
if __name__ == '__main__':
    # List of example
    #You can save this list as .txt file,open and access each link,,but for rigurous testing puropse i have done this
    urls = [
        "https://www.google.com",
        "https://www.amazon.com",
        "https://www.apple.com",
        "https://www.microsoft.com",
        "https://www.wikipedia.org",
        "https://www.reddit.com",
        "https://www.nytimes.com",
        "https://www.youtube.com",
        "https://www.facebook.com",
        "https://www.twitter.com",
        "https://www.instagram.com",
        "https://www.linkedin.com",
        "https://www.netflix.com",
        "https://www.pinterest.com",
        "https://www.spotify.com",
        "https://www.bbc.co.uk",
        "https://www.cnn.com",
        "https://www.ebay.com",
        "https://www.yahoo.com",
        "https://www.github.com",
        "https://www.stackoverflow.com",
        "https://www.medium.com",
        "https://www.quora.com",
        "https://www.aliexpress.com",
        "https://www.aliyun.com",
        "https://www.foxnews.com",
        "https://www.theguardian.com",
        "https://www.washingtonpost.com",
        "https://www.forbes.com",
        "https://www.imdb.com",
        "https://www.livejournal.com",
        "https://www.minecraft.net",
        "https://www.npr.org",
        "https://www.rottentomatoes.com",
        "https://www.thesaurus.com",
        "https://www.twitch.tv",
        "https://www.weather.com",
        "https://www.whitehouse.gov",
        "https://www.xbox.com",
        "https://www.yelp.com",
        "https://www.zillow.com",
        "https://www.ancestry.com",
        "https://www.booking.com",
        "https://www.chase.com",
        "https://www.dropbox.com",
        "https://www.espn.com",
        "https://www.flickr.com",
        "https://www.gmail.com",
        "https://www.hulu.com",
        "https://www.icloud.com",
        "https://www.jetbrains.com",
        "https://www.khanacademy.org",
        "https://www.livescience.com",
        "https://www.mozilla.org",
        "https://www.netflix.com",
        "https://www.opera.com",
        "https://www.pixabay.com",
        "https://www.quicksilver.com",
        "https://www.redcross.org",
        "https://www.squarespace.com",
        "https://www.twitch.tv",
        "https://www.udacity.com",
        "https://www.vanguard.com",
        "https://www.weather.com",
        "https://www.xkcd.com",
        "https://www.youtube.com",
        "https://www.zara.com",
        "https://www.aol.com",
        "https://www.bestbuy.com",
        "https://www.craigslist.org",
        "https://www.dailymotion.com",
        "https://www.eonline.com",
        "https://www.fandango.com",
        "https://www.goodreads.com",
        "https://www.huffpost.com",
        "https://www.ign.com",
        "https://www.justice.gov",
        "https://www.kotaku.com",
        "https://www.last.fm",
        "https://www.myspace.com",
        "https://www.netflix.com",
        "https://www.oreilly.com",
        "https://www.pcmag.com",
        "https://www.quizlet.com",
        "https://www.reuters.com",
        "https://www.samsung.com",
        "https://www.theatlantic.com",
        "https://www.upwork.com",
        "https://www.vimeo.com",
        "https://www.walmart.com",
        "https://www.xfinity.com",
        "https://www.yahoo.com",
        "https://www.zappos.com"
    ]


    data = []#contains list of dictionary
    for url in urls:
        result = scrape_website(url)#Function Call for scraping each web site one-by-one
        if result:
            data.append(result)#appending result in data as dictionary

    # Convert to DataFrame
    df = pd.DataFrame(data)
    print(df)

    # Save DataFrame to a CSV file
    df.to_csv('websites_info.csv', index=False)
