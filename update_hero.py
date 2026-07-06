import sys, re

file_path = '/home/ali/Music/360EliteDesign.com/index.html'

try:
    with open(file_path, 'r') as f:
        content = f.read()

    # Pattern matches from the start of the hero section to its closing </section>
    hero_pattern = re.compile(r'<!-- Bright Premium Sexy Abstract Hero Section -->.*?</section>', re.DOTALL)
    
    new_hero = """<!-- Cinematic Exploding Hero Section -->
    <section class="hero" id="home" style="min-height: 100vh; position: relative; display: flex; align-items: center; overflow: hidden; perspective: 1500px;">
        
        <!-- Exploding Background Image (Bright Agency Workspace) -->
        <div id="hero-bg" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-image: url('https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=2670&auto=format&fit=crop'); background-size: cover; background-position: center; z-index: 0; transform-origin: center; transition: transform 0.1s ease-out;"></div>
        
        <!-- Bright Glass Overlay -->
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(135deg, rgba(255, 255, 255, 0.9) 0%, rgba(240, 248, 255, 0.6) 50%, rgba(0, 198, 255, 0.2) 100%); z-index: 1; backdrop-filter: blur(8px);"></div>
        
        <div class="container" id="hero-content-wrapper" style="position: relative; z-index: 2; width: 100%; max-width: 1400px; padding: 0 20px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; margin-top: 80px;">
            
            <!-- Left Content: Crisp HTML Text -->
            <div id="hero-left-text" style="flex: 1; min-width: 300px; max-width: 650px; transform-origin: left center; transition: transform 0.1s ease-out, opacity 0.1s ease-out;">
                <h1 style="color: #0A192F; font-size: clamp(3.5rem, 5vw, 5.5rem); font-weight: 800; line-height: 1.1; margin-bottom: 1.5rem; font-family: 'Outfit', sans-serif;">
                    ELEVATE YOUR BRAND'S <br><span style="background: linear-gradient(to right, #007BFF, #00C6FF); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">DIGITAL EXPERIENCE</span>
                </h1>
                <p style="color: #475569; font-size: 1.3rem; margin-bottom: 2.5rem; max-width: 500px; line-height: 1.6; font-weight: 500;">
                    From Vision to Reality: Comprehensive Design & Development Solutions built perfectly for the modern web.
                </p>
                <div style="display: flex; gap: 1.5rem; flex-wrap: wrap;">
                    <a href="#services" class="btn" style="background: linear-gradient(135deg, #007BFF, #00C6FF); color: white; border-radius: 30px; padding: 18px 40px; font-weight: 700; box-shadow: 0 10px 30px rgba(0, 123, 255, 0.4); display: flex; align-items: center; gap: 10px; font-size: 1.1rem;">
                        EXPLORE OUR SERVICES <i class="ph-bold ph-arrow-right"></i>
                    </a>
                    <a href="#portfolio" class="btn" style="background: white; border: 2px solid rgba(0,0,0,0.1); color: #0A192F; border-radius: 30px; padding: 18px 40px; font-weight: 800; box-shadow: 0 10px 25px rgba(0,0,0,0.05); font-size: 1.1rem;">
                        VIEW PORTFOLIO
                    </a>
                </div>
            </div>

            <!-- Right Content: Exploding Glass Cards -->
            <div id="hero-right-cards" style="flex: 1; min-width: 300px; position: relative; height: 500px; display: flex; justify-content: center; align-items: center; transform-style: preserve-3d;">
                
                <div class="explode-card" data-x="250" data-y="-150" data-z="300" data-rot="25" style="position: absolute; top: 15%; right: 15%; background: rgba(255,255,255,0.85); backdrop-filter: blur(25px); border: 1px solid rgba(255,255,255,1); padding: 30px 35px; border-radius: 24px; box-shadow: 0 25px 50px rgba(0,123,255,0.15); display: flex; flex-direction: column; align-items: center; gap: 15px; z-index: 3; transition: transform 0.1s ease-out, opacity 0.1s ease-out;">
                    <div style="width: 70px; height: 70px; background: rgba(0,123,255,0.1); border-radius: 20px; display: flex; align-items: center; justify-content: center;">
                        <i class="ph-bold ph-layout" style="font-size: 2.5rem; color: #007BFF;"></i>
                    </div>
                    <span style="color: #0A192F; font-weight: 800; font-size: 0.95rem; letter-spacing: 1px;">WEB DESIGN</span>
                </div>

                <div class="explode-card" data-x="-300" data-y="-100" data-z="400" data-rot="-35" style="position: absolute; top: 45%; left: 5%; background: rgba(255,255,255,0.95); backdrop-filter: blur(20px); border: 1px solid white; padding: 25px 30px; border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.08); display: flex; flex-direction: column; align-items: center; gap: 12px; z-index: 2; transition: transform 0.1s ease-out, opacity 0.1s ease-out;">
                    <div style="width: 60px; height: 60px; background: #00C6FF; border-radius: 16px; display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 25px rgba(0,198,255,0.4);">
                        <i class="ph-bold ph-bezier-curve" style="font-size: 2rem; color: white;"></i>
                    </div>
                    <span style="color: #0A192F; font-weight: 800; font-size: 0.9rem; letter-spacing: 1px;">UI/UX</span>
                </div>

                <div class="explode-card" data-x="180" data-y="250" data-z="500" data-rot="45" style="position: absolute; bottom: 10%; right: 25%; background: rgba(255,255,255,0.7); backdrop-filter: blur(30px); border: 1px solid rgba(255,255,255,0.8); padding: 35px 40px; border-radius: 24px; box-shadow: 0 30px 60px rgba(0,123,255,0.2); display: flex; flex-direction: column; align-items: center; gap: 15px; z-index: 4; transition: transform 0.1s ease-out, opacity 0.1s ease-out;">
                    <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #0A192F, #112240); border-radius: 24px; display: flex; align-items: center; justify-content: center; box-shadow: 0 15px 30px rgba(10,25,47,0.4);">
                        <i class="ph-bold ph-trend-up" style="font-size: 3rem; color: #00C6FF;"></i>
                    </div>
                    <span style="color: #0A192F; font-weight: 800; font-size: 1rem; letter-spacing: 1.5px;">MARKETING</span>
                </div>

            </div>
        </div>
    </section>

    <!-- Scroll Explosion Cinematic Logic -->
    <script>
        document.addEventListener('scroll', () => {
            const scrollY = window.scrollY;
            const heroHeight = window.innerHeight;
            
            // Limit effect to when hero is visible
            if (scrollY <= heroHeight) {
                const progress = scrollY / heroHeight; // 0 to 1
                const easeProgress = Math.pow(progress, 1.5); // Smoother acceleration
                
                // 1. Zoom Background
                const bg = document.getElementById('hero-bg');
                if (bg) {
                    const bgScale = 1 + (easeProgress * 0.8); // Zooms up significantly
                    bg.style.transform = `scale(${bgScale})`;
                }

                // 2. Fade & Move Left Text Out
                const text = document.getElementById('hero-left-text');
                if (text) {
                    const textMoveX = easeProgress * -300; 
                    const textScale = 1 - (easeProgress * 0.2);
                    const opacity = 1 - (progress * 1.5);
                    text.style.transform = `translateX(${textMoveX}px) scale(${textScale})`;
                    text.style.opacity = opacity > 0 ? opacity : 0;
                }

                // 3. Explode Right Cards into the camera (3D space)
                const cards = document.querySelectorAll('.explode-card');
                cards.forEach(card => {
                    const tx = parseFloat(card.getAttribute('data-x')) * easeProgress;
                    const ty = parseFloat(card.getAttribute('data-y')) * easeProgress;
                    const tz = parseFloat(card.getAttribute('data-z')) * easeProgress;
                    const rot = parseFloat(card.getAttribute('data-rot')) * easeProgress;
                    
                    const scale = 1 + (easeProgress * 1.5); // Massively scale up as they explode
                    const opacity = 1 - (progress * 1.5);
                    
                    card.style.transform = `translate3d(${tx}px, ${ty}px, ${tz}px) rotateZ(${rot}deg) scale(${scale})`;
                    card.style.opacity = opacity > 0 ? opacity : 0;
                });
            }
        });
    </script>"""

    if hero_pattern.search(content):
        content = hero_pattern.sub(new_hero, content, count=1)
        with open(file_path, 'w') as f:
            f.write(content)
        print("Successfully injected Cinematic Exploding Hero!")
    else:
        print("Hero section not found.")

except Exception as e:
    print(e)
