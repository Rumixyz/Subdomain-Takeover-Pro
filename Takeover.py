import dns.resolver
import requests
import sys

# Fingerprints - Ye services vulnerable hoti hain
FINGERPRINTS = {
    "AWS S3": "NoSuchBucket",
    "GitHub Pages": "There isn't a GitHub Pages site here",
    "Heroku": "No such app",
    "Shopify": "Sorry, this shop is currently unavailable",
    "Surge.sh": "project not found",
    "Pantheon": "The gods are wise",
    "Tumblr": "There's nothing here"
}

def check_takeover(subdomain):
    try:
        # CNAME nikal
        answers = dns.resolver.resolve(subdomain, 'CNAME')
        for rdata in answers:
            cname = str(rdata.target).rstrip('.')
            print(f"[+] {subdomain} → CNAME → {cname}")
            
            # Har fingerprint check kar
            try:
                r = requests.get(f"http://{subdomain}", timeout=5)
                for service, fingerprint in FINGERPRINTS.items():
                    if fingerprint in r.text:
                        print(f"🚨 TAKEOVER POSSIBLE! Service: {service}")
                        print(f" Proof: Response contains '{fingerprint}'")
                        print(f" Next: Claim '{cname}' on {service}")
                        return True
            except: pass
    except: pass
    return False

if __name__ == "__main__":
    if len(sys.argv)!= 2:
        print("Usage: python3 takeover.py subdomains.txt")
        sys.exit()
    
    with open(sys.argv[1], 'r') as f:
        subs = f.read().splitlines()
    
    print(f"Scanning {len(subs)} subdomains for takeovers...\n")
    for sub in subs:
        check_takeover(sub.strip())
