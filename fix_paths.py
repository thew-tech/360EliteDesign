file_path = '/home/ali/Music/360EliteDesign.com/index.html'
with open(file_path, 'r') as f:
    content = f.read()

replacements = [
    # Logo
    ('src="logo.jpg"', 'src="/logo.jpg"'),
    
    # Hero background
    ("url('images/hero-team.jpg')", "url('/images/hero-team.jpg')"),
    
    # Service flip cards
    ("url('images/service-webdesign.jpg')", "url('/images/service-webdesign.jpg')"),
    ("url('images/service-uiux.jpg')", "url('/images/service-uiux.jpg')"),
    ("url('images/service-branding.jpg')", "url('/images/service-branding.jpg')"),
    ("url('images/service-ecommerce.jpg')", "url('/images/service-ecommerce.jpg')"),
    ("url('images/service-marketing.jpg')", "url('/images/service-marketing.jpg')"),
    ("url('images/service-mobileapp.jpg')", "url('/images/service-mobileapp.jpg')"),
    
    # Portfolio images
    ('src="images/portfolio-webdesign.jpg"', 'src="/images/portfolio-webdesign.jpg"'),
    ('src="images/portfolio-branding.jpg"', 'src="/images/portfolio-branding.jpg"'),
    
    # Artifact absolute paths -> local
    ('src="/home/ali/.gemini/antigravity/brain/6756adbf-4204-4133-8c0f-5f6ee288b176/about_us_team_1778866850726.png"', 'src="/images/about-us-team.png"'),
    ('src="/home/ali/.gemini/antigravity/brain/6756adbf-4204-4133-8c0f-5f6ee288b176/headshot_1_1778866257706.png"', 'src="/images/headshot.png"'),
    ('src="/home/ali/.gemini/antigravity/brain/6756adbf-4204-4133-8c0f-5f6ee288b176/portfolio_app_1778866339648.png"', 'src="/images/portfolio-app.png"'),
    ('src="/home/ali/.gemini/antigravity/brain/6756adbf-4204-4133-8c0f-5f6ee288b176/portfolio_web_1778866193412.png"', 'src="/images/portfolio-web.png"'),
]

count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        count += 1
        print(f'Fixed: {old[:50]} -> {new}')
    else:
        print(f'Not found: {old[:60]}')

with open(file_path, 'w') as f:
    f.write(content)

print(f'\nTotal: {count} paths fixed for Netlify deployment!')
