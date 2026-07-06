import re

file_path = '/home/ali/Music/360EliteDesign.com/index.html'

with open(file_path, 'r') as f:
    content = f.read()

# 1. Add Sarah Jenkins headshot to hero right side (replace the marketing card area)
old_marketing_card = '''<div class="mouse-parallax" data-speed="-8" style="position: absolute; bottom: 10%; right: 25%; background: rgba(255,255,255,0.7); backdrop-filter: blur(30px); border: 1px solid rgba(255,255,255,0.8); padding: 35px 40px; border-radius: 24px; box-shadow: 0 30px 60px rgba(0,123,255,0.2); display: flex; flex-direction: column; align-items: center; gap: 15px; z-index: 4; transition: transform 0.1s ease-out;">
                    <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #0A192F, #112240); border-radius: 24px; display: flex; align-items: center; justify-content: center; box-shadow: 0 15px 30px rgba(10,25,47,0.4);">
                        <i class="ph ph-trend-up" style="font-size: 3rem; color: #00C6FF;"></i>
                    </div>
                    <span style="color: #0A192F; font-weight: 800; font-size: 1rem; letter-spacing: 1.5px;">MARKETING</span>
                </div>'''

new_hero_image = '''<div class="mouse-parallax" data-speed="-8" style="position: absolute; bottom: 5%; right: 10%; z-index: 4; transition: transform 0.1s ease-out;">
                    <div style="width: 220px; height: 280px; border-radius: 28px; overflow: hidden; box-shadow: 0 30px 60px rgba(0,123,255,0.25); border: 3px solid rgba(255,255,255,0.9); position: relative;">
                        <img src="images/headshot.png" alt="Creative Director" style="width: 100%; height: 100%; object-fit: cover;">
                        <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 15px 20px; background: linear-gradient(to top, rgba(10,25,47,0.9), transparent); text-align: center;">
                            <span style="color: white; font-weight: 700; font-size: 0.85rem; font-family: 'Outfit', sans-serif; letter-spacing: 1px;">CREATIVE DIRECTOR</span>
                        </div>
                    </div>
                </div>'''

if old_marketing_card in content:
    content = content.replace(old_marketing_card, new_hero_image)
    print("1. Added Sarah Jenkins headshot to hero ✓")
else:
    print("1. Marketing card not found (may already be changed)")

# 2. Add scrolling services marquee banner between hero and services
marquee_banner = '''
    <!-- Scrolling Services Marquee Banner -->
    <div style="background: linear-gradient(135deg, #0A192F, #112240); padding: 20px 0; overflow: hidden; position: relative;">
        <div style="display: flex; gap: 60px; animation: services-marquee 25s linear infinite; width: max-content; align-items: center;">
            <span style="color: white; font-size: 1.1rem; font-weight: 700; font-family: 'Outfit', sans-serif; letter-spacing: 3px; white-space: nowrap; text-transform: uppercase;">✦ WEB DESIGN</span>
            <span style="color: #00C6FF; font-size: 1.1rem; font-weight: 700; font-family: 'Outfit', sans-serif; letter-spacing: 3px; white-space: nowrap; text-transform: uppercase;">✦ UI/UX DESIGN</span>
            <span style="color: white; font-size: 1.1rem; font-weight: 700; font-family: 'Outfit', sans-serif; letter-spacing: 3px; white-space: nowrap; text-transform: uppercase;">✦ BRAND IDENTITY</span>
            <span style="color: #007BFF; font-size: 1.1rem; font-weight: 700; font-family: 'Outfit', sans-serif; letter-spacing: 3px; white-space: nowrap; text-transform: uppercase;">✦ E-COMMERCE</span>
            <span style="color: white; font-size: 1.1rem; font-weight: 700; font-family: 'Outfit', sans-serif; letter-spacing: 3px; white-space: nowrap; text-transform: uppercase;">✦ DIGITAL MARKETING</span>
            <span style="color: #00C6FF; font-size: 1.1rem; font-weight: 700; font-family: 'Outfit', sans-serif; letter-spacing: 3px; white-space: nowrap; text-transform: uppercase;">✦ SEO OPTIMIZATION</span>
            <span style="color: white; font-size: 1.1rem; font-weight: 700; font-family: 'Outfit', sans-serif; letter-spacing: 3px; white-space: nowrap; text-transform: uppercase;">✦ MOBILE APPS</span>
            <span style="color: #007BFF; font-size: 1.1rem; font-weight: 700; font-family: 'Outfit', sans-serif; letter-spacing: 3px; white-space: nowrap; text-transform: uppercase;">✦ GROWTH STRATEGY</span>
            <!-- Duplicate for seamless loop -->
            <span style="color: white; font-size: 1.1rem; font-weight: 700; font-family: 'Outfit', sans-serif; letter-spacing: 3px; white-space: nowrap; text-transform: uppercase;">✦ WEB DESIGN</span>
            <span style="color: #00C6FF; font-size: 1.1rem; font-weight: 700; font-family: 'Outfit', sans-serif; letter-spacing: 3px; white-space: nowrap; text-transform: uppercase;">✦ UI/UX DESIGN</span>
            <span style="color: white; font-size: 1.1rem; font-weight: 700; font-family: 'Outfit', sans-serif; letter-spacing: 3px; white-space: nowrap; text-transform: uppercase;">✦ BRAND IDENTITY</span>
            <span style="color: #007BFF; font-size: 1.1rem; font-weight: 700; font-family: 'Outfit', sans-serif; letter-spacing: 3px; white-space: nowrap; text-transform: uppercase;">✦ E-COMMERCE</span>
            <span style="color: white; font-size: 1.1rem; font-weight: 700; font-family: 'Outfit', sans-serif; letter-spacing: 3px; white-space: nowrap; text-transform: uppercase;">✦ DIGITAL MARKETING</span>
            <span style="color: #00C6FF; font-size: 1.1rem; font-weight: 700; font-family: 'Outfit', sans-serif; letter-spacing: 3px; white-space: nowrap; text-transform: uppercase;">✦ SEO OPTIMIZATION</span>
            <span style="color: white; font-size: 1.1rem; font-weight: 700; font-family: 'Outfit', sans-serif; letter-spacing: 3px; white-space: nowrap; text-transform: uppercase;">✦ MOBILE APPS</span>
            <span style="color: #007BFF; font-size: 1.1rem; font-weight: 700; font-family: 'Outfit', sans-serif; letter-spacing: 3px; white-space: nowrap; text-transform: uppercase;">✦ GROWTH STRATEGY</span>
        </div>
        <style>
            @keyframes services-marquee {
                0% { transform: translateX(0); }
                100% { transform: translateX(-50%); }
            }
        </style>
    </div>

'''

# Insert marquee between hero </section> and services section
target = '    <!-- 3D Flipping Photo Cards Services Section -->'
if target in content:
    content = content.replace(target, marquee_banner + target)
    print("2. Added scrolling services marquee banner ✓")
else:
    print("2. Could not find services section marker")

# 3. Add scroll-based exploding effect to hero
explode_script = '''
    <!-- Hero Scroll Explode Effect -->
    <script>
        (function() {
            const hero = document.getElementById('home');
            if (!hero) return;
            
            const heroContent = hero.querySelector('.container');
            const heroBg = hero;
            
            window.addEventListener('scroll', () => {
                const scrollY = window.scrollY;
                const heroH = hero.offsetHeight;
                
                if (scrollY <= heroH) {
                    const progress = scrollY / heroH;
                    const ease = Math.pow(progress, 1.3);
                    
                    // Scale background slightly
                    heroBg.style.backgroundSize = (100 + ease * 30) + '%';
                    
                    // Fade and move content
                    if (heroContent) {
                        heroContent.style.opacity = Math.max(0, 1 - progress * 1.8);
                        heroContent.style.transform = 'translateY(' + (ease * -80) + 'px) scale(' + (1 - ease * 0.1) + ')';
                    }
                    
                    // Explode the parallax cards outward
                    const cards = hero.querySelectorAll('.mouse-parallax');
                    cards.forEach((card, i) => {
                        const directions = [
                            { x: 200, y: -150, rot: 15 },
                            { x: -250, y: -100, rot: -20 },
                            { x: 150, y: 200, rot: 25 }
                        ];
                        const dir = directions[i % 3];
                        const tx = dir.x * ease;
                        const ty = dir.y * ease;
                        const rot = dir.rot * ease;
                        const scale = 1 + ease * 0.5;
                        const opacity = Math.max(0, 1 - progress * 2);
                        
                        card.style.transform = 'translate(' + tx + 'px, ' + ty + 'px) rotate(' + rot + 'deg) scale(' + scale + ')';
                        card.style.opacity = opacity;
                    });
                }
            });
        })();
    </script>
'''

# Insert before the closing </body>
content = content.replace('</body>', explode_script + '</body>')
print("3. Added hero scroll explode effect ✓")

with open(file_path, 'w') as f:
    f.write(content)

print("\nAll 3 upgrades applied successfully!")
