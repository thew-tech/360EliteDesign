import re

file_path = '/home/ali/Music/360EliteDesign.com/index.html'

with open(file_path, 'r') as f:
    content = f.read()

# Find and replace the new cinematic hero + its script block
old_pattern = re.compile(
    r'<!-- Cinematic Exploding Hero Section -->.*?</section>\s*<!-- Scroll Explosion Cinematic Logic -->.*?</script>',
    re.DOTALL
)

restored_hero = """<!-- Bright Premium Sexy Abstract Hero Section -->
    <section class="hero" id="home" style="background-image: url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=2564&auto=format&fit=crop'); background-size: cover; background-position: center; min-height: 100vh; position: relative; display: flex; align-items: center; overflow: hidden; perspective: 1000px;">
        
        <!-- Bright Sexy Pulsing Glass Overlay -->
        <div class="animate-pulse" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(135deg, rgba(255, 255, 255, 0.75) 0%, rgba(240, 248, 255, 0.4) 50%, rgba(0, 198, 255, 0.15) 100%); z-index: 1; backdrop-filter: blur(8px);"></div>
        
        <div class="container" style="position: relative; z-index: 2; width: 100%; max-width: 1400px; padding: 0 20px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; margin-top: 80px;">
            
            <!-- Left Content: Crisp HTML Text -->
            <div style="flex: 1; min-width: 300px; max-width: 650px; transition: transform 0.1s ease-out;" class="mouse-parallax" data-speed="2">
                <h1 style="color: #0A192F; font-size: clamp(3.5rem, 5vw, 5.5rem); font-weight: 800; line-height: 1.1; margin-bottom: 1.5rem; font-family: 'Outfit', sans-serif;">
                    ELEVATE YOUR BRAND'S <br><span style="background: linear-gradient(to right, #007BFF, #00C6FF); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">DIGITAL EXPERIENCE</span>
                </h1>
                <p style="color: #475569; font-size: 1.3rem; margin-bottom: 2.5rem; max-width: 500px; line-height: 1.6; font-weight: 500;">
                    From Vision to Reality: Comprehensive Design & Development Solutions built perfectly for the modern web.
                </p>
                <div style="display: flex; gap: 1.5rem; flex-wrap: wrap;">
                    <a href="#services" class="btn" style="background: linear-gradient(135deg, #007BFF, #00C6FF); color: white; border-radius: 30px; padding: 18px 40px; font-weight: 700; box-shadow: 0 10px 30px rgba(0, 123, 255, 0.4); display: flex; align-items: center; gap: 10px; font-size: 1.1rem;">
                        EXPLORE OUR SERVICES <i class="ph ph-arrow-right"></i>
                    </a>
                    <a href="#portfolio" class="btn" style="background: white; border: 2px solid rgba(0,0,0,0.1); color: #0A192F; border-radius: 30px; padding: 18px 40px; font-weight: 800; box-shadow: 0 10px 25px rgba(0,0,0,0.05); font-size: 1.1rem;">
                        VIEW PORTFOLIO
                    </a>
                </div>
            </div>

            <!-- Right Content: Mouse-Reactive Glass Cards -->
            <div style="flex: 1; min-width: 300px; position: relative; height: 500px; display: flex; justify-content: center; align-items: center;">
                
                <div class="mouse-parallax" data-speed="-5" style="position: absolute; top: 15%; right: 15%; background: rgba(255,255,255,0.85); backdrop-filter: blur(25px); border: 1px solid rgba(255,255,255,0.9); padding: 30px 35px; border-radius: 24px; box-shadow: 0 25px 50px rgba(0,123,255,0.15); display: flex; flex-direction: column; align-items: center; gap: 15px; z-index: 3; transition: transform 0.1s ease-out;">
                    <div style="width: 70px; height: 70px; background: rgba(0,123,255,0.1); border-radius: 20px; display: flex; align-items: center; justify-content: center;">
                        <i class="ph ph-layout" style="font-size: 2.5rem; color: #007BFF;"></i>
                    </div>
                    <span style="color: #0A192F; font-weight: 800; font-size: 0.95rem; letter-spacing: 1px;">WEB DESIGN</span>
                </div>

                <div class="mouse-parallax" data-speed="4" style="position: absolute; top: 45%; left: 5%; background: rgba(255,255,255,0.95); backdrop-filter: blur(20px); border: 1px solid white; padding: 25px 30px; border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.08); display: flex; flex-direction: column; align-items: center; gap: 12px; z-index: 2; transition: transform 0.1s ease-out;">
                    <div style="width: 60px; height: 60px; background: #00C6FF; border-radius: 16px; display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 25px rgba(0,198,255,0.4);">
                        <i class="ph ph-bezier-curve" style="font-size: 2rem; color: white;"></i>
                    </div>
                    <span style="color: #0A192F; font-weight: 800; font-size: 0.9rem; letter-spacing: 1px;">UI/UX</span>
                </div>

                <div class="mouse-parallax" data-speed="-8" style="position: absolute; bottom: 10%; right: 25%; background: rgba(255,255,255,0.7); backdrop-filter: blur(30px); border: 1px solid rgba(255,255,255,0.8); padding: 35px 40px; border-radius: 24px; box-shadow: 0 30px 60px rgba(0,123,255,0.2); display: flex; flex-direction: column; align-items: center; gap: 15px; z-index: 4; transition: transform 0.1s ease-out;">
                    <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #0A192F, #112240); border-radius: 24px; display: flex; align-items: center; justify-content: center; box-shadow: 0 15px 30px rgba(10,25,47,0.4);">
                        <i class="ph ph-trend-up" style="font-size: 3rem; color: #00C6FF;"></i>
                    </div>
                    <span style="color: #0A192F; font-weight: 800; font-size: 1rem; letter-spacing: 1.5px;">MARKETING</span>
                </div>

            </div>
        </div>
    </section>"""

if old_pattern.search(content):
    content = old_pattern.sub(restored_hero, content, count=1)
    with open(file_path, 'w') as f:
        f.write(content)
    print("SUCCESS: Hero reverted back to the bright abstract version!")
else:
    print("Could not find the cinematic hero to revert.")
