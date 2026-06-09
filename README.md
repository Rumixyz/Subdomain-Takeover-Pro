# Subdomain Takeover Pro 🚨

Find subdomain takeovers in seconds. One takeover = $500 to $10,000 bug bounty.

### Install
```bash`
git clone https://github.com/Rumixyz/subdomain-takeover-pro.git
cd subdomain-takeover-pro
pip install -r requirements.txt
```
### Usage
1. List the subdomains in `subdomains.txt`
2. Run the tool:
```bash`
python3 takeover.py subdomains.txt
````
### Example subdomains.txt
````
blog.doppler.com
docs.doppler.com
app.doppler.com
````
### What it finds
Detects vulnerable CNAMEs for:
- AWS S3 buckets
- GitHub Pages
- Heroku Apps
- Shopify
- Surge.sh
- Pantheon
- Tumblr

### Example Output
`````
[+] Checking blog.doppler.com
[+] CNAME found: blog.doppler.com -> old-bucket.s3.amazonaws.com
🚨 TAKEOVER POSSIBLE! Error: NoSuchBucket

[+] Checking docs.doppler.com
[-] Safe - no takeover found
````
### Legal Disclaimer
This tool is for educational purposes and authorized testing only.
Only scan domains where you have explicit written permission.
I am not responsible for illegal use.

### Sponsor Me
If this tool helped you earn a bounty, consider [sponsoring me](https://github.com/sponsors/Rumixyz) ❤️



