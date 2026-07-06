import re

file_path = '/home/ali/Music/360EliteDesign.com/index.html'

with open(file_path, 'r') as f:
    content = f.read()

# Replace the entire right-side hero cards area with a richer image gallery
old_right = '''<!-- Right Content: Mouse-Reactive Glass Cards -->
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

                <div class="mouse-parallax" data-speed="-8" style="position: absolute; bottom: 5%; right: 10%; z-index: 4; transition: transform 0.1s ease-out;">
                    <div style="width: 220px; height: 280px; border-radius: 28px; overflow: hidden; box-shadow: 0 30px 60px rgba(0,123,255,0.25); border: 3px solid rgba(255,255,255,0.9); position: relative;">
                        <img src="images/headshot.png" alt="Creative Director" style="width: 100%; height: 100%; object-fit: cover;">
                        <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 15px 20px; background: linear-gradient(to top, rgba(10,25,47,0.9), transparent); text-align: center;">
                            <span style="color: white; font-weight: 700; font-size: 0.85rem; font-family: 'Outfit', sans-serif; letter-spacing: 1px;">CREATIVE DIRECTOR</span>
                        </div>
                    </div>
                </div>

            </div>'''

new_right = '''<!-- Right Content: Rich Floating Image Gallery -->
            <div style="flex: 1; min-width: 300px; position: relative; height: 550px; display: flex; justify-content: center; align-items: center;">
                
                <!-- Main Portfolio Showcase (Large) -->
                <div class="mouse-parallax hero-float-1" data-speed="-3" style="position: absolute; top: 5%; right: 5%; z-index: 5; transition: transform 0.1s ease-out;">
                    <div style="width: 280px; height: 200px; border-radius: 24px; overflow: hidden; box-shadow: 0 30px 60px rgba(0,123,255,0.25); border: 3px solid rgba(255,255,255,0.9); position: relative;">
                        <img src="images/portfolio-web.png" alt="Web Project" style="width: 100%; height: 100%; object-fit: cover;">
                        <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 12px 16px; background: linear-gradient(to top, rgba(10,25,47,0.9), transparent);">
                            <span style="color: white; font-weight: 700; font-size: 0.8rem; font-family: 'Outfit', sans-serif; letter-spacing: 1px;">WEB DEVELOPMENT</span>
                        </div>
                    </div>
                </div>

                <!-- App Design Card -->
                <div class="mouse-parallax hero-float-2" data-speed="5" style="position: absolute; top: 42%; left: 0%; z-index: 3; transition: transform 0.1s ease-out;">
                    <div style="width: 200px; height: 160px; border-radius: 20px; overflow: hidden; box-shadow: 0 25px 50px rgba(0,198,255,0.2); border: 3px solid rgba(255,255,255,0.9); position: relative;">
                        <img src="images/portfolio-app.png" alt="App Design" style="width: 100%; height: 100%; object-fit: cover;">
                        <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 10px 14px; background: linear-gradient(to top, rgba(10,25,47,0.9), transparent);">
                            <span style="color: white; font-weight: 700; font-size: 0.75rem; font-family: 'Outfit', sans-serif; letter-spacing: 1px;">APP DESIGN</span>
                        </div>
                    </div>
                </div>

                <!-- Sarah Jenkins Headshot -->
                <div class="mouse-parallax hero-float-3" data-speed="-6" style="position: absolute; bottom: 2%; right: 30%; z-index: 6; transition: transform 0.1s ease-out;">
                    <div style="width: 160px; height: 210px; border-radius: 24px; overflow: hidden; box-shadow: 0 25px 50px rgba(0,123,255,0.3); border: 3px solid rgba(255,255,255,0.9); position: relative;">
                        <img src="images/headshot.png" alt="Creative Director" style="width: 100%; height: 100%; object-fit: cover;">
                        <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 12px 14px; background: linear-gradient(to top, rgba(10,25,47,0.9), transparent); text-align: center;">
                            <span style="color: white; font-weight: 700; font-size: 0.75rem; font-family: 'Outfit', sans-serif; letter-spacing: 1px;">CREATIVE LEAD</span>
                        </div>
                    </div>
                </div>

                <!-- Branding Card -->
                <div class="mouse-parallax hero-float-4" data-speed="3" style="position: absolute; bottom: 8%; right: 2%; z-index: 4; transition: transform 0.1s ease-out;">
                    <div style="width: 180px; height: 140px; border-radius: 20px; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.15); border: 3px solid rgba(255,255,255,0.9); position: relative;">
                        <img src="images/portfolio-branding.jpg" alt="Branding" style="width: 100%; height: 100%; object-fit: cover;">
                        <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 10px 14px; background: linear-gradient(to top, rgba(10,25,47,0.9), transparent);">
                            <span style="color: white; font-weight: 700; font-size: 0.75rem; font-family: 'Outfit', sans-serif; letter-spacing: 1px;">BRANDING</span>
                        </div>
                    </div>
                </div>

                <!-- Floating Stats Badge -->
                <div class="mouse-parallax hero-float-5" data-speed="-4" style="position: absolute; top: 30%; right: 35%; z-index: 7; transition: transform 0.1s ease-out;">
                    <div style="width: 110px; height: 110px; border-radius: 50%; background: linear-gradient(135deg, #007BFF, #00C6FF); display: flex; flex-direction: column; align-items: center; justify-content: center; box-shadow: 0 20px 40px rgba(0,123,255,0.4); border: 3px solid rgba(255,255,255,0.3);">
                        <span style="color: white; font-weight: 900; font-size: 1.8rem; font-family: 'Outfit', sans-serif; line-height: 1;">150+</span>
                        <span style="color: rgba(255,255,255,0.8); font-weight: 600; font-size: 0.65rem; font-family: 'Outfit', sans-serif; letter-spacing: 1px; text-transform: uppercase;">Projects</span>
                    </div>
                </div>

                <!-- Floating UI/UX Glass Card -->
                <div class="mouse-parallax hero-float-6" data-speed="7" style="position: absolute; top: 12%; left: 15%; z-index: 2; transition: transform 0.1s ease-out;">
                    <div style="background: rgba(255,255,255,0.9); backdrop-filter: blur(20px); border: 1px solid white; padding: 18px 22px; border-radius: 18px; box-shadow: 0 15px 30px rgba(0,0,0,0.08); display: flex; align-items: center; gap: 12px;">
                        <div style="width: 45px; height: 45px; background: #00C6FF; border-radius: 14px; display: flex; align-items: center; justify-content: center; box-shadow: 0 8px 20px rgba(0,198,255,0.3);">
                            <i class="ph-bold ph-star" style="font-size: 1.3rem; color: white;"></i>
                        </div>
                        <div>
                            <span style="color: #0A192F; font-weight: 800; font-size: 0.85rem; font-family: 'Outfit', sans-serif; display: block;">5.0 Rating</span>
                            <span style="color: #64748b; font-weight: 500; font-size: 0.7rem; font-family: 'Inter', sans-serif;">98% Satisfaction</span>
                        </div>
                    </div>
                </div>

            </div>'''

if old_right in content:
    content = content.replace(old_right, new_right)
    print("1. Replaced hero right side with rich image gallery ✓")
else:
    print("1. Could not find exact hero right side to replace")

# 2. Add floating animation CSS
float_css = '''
    <!-- Hero Floating Animations -->
    <style>
        .hero-float-1 { animation: heroFloat1 6s ease-in-out infinite; }
        .hero-float-2 { animation: heroFloat2 5s ease-in-out infinite; }
        .hero-float-3 { animation: heroFloat3 7s ease-in-out infinite; }
        .hero-float-4 { animation: heroFloat4 5.5s ease-in-out infinite; }
        .hero-float-5 { animation: heroFloat5 4s ease-in-out infinite; }
        .hero-float-6 { animation: heroFloat6 6.5s ease-in-out infinite; }

        @keyframes heroFloat1 {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-18px) rotate(2deg); }
        }
        @keyframes heroFloat2 {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-14px) rotate(-3deg); }
        }
        @keyframes heroFloat3 {
            0%, 100% { transform: translateY(0px) scale(1); }
            50% { transform: translateY(-20px) scale(1.03); }
        }
        @keyframes heroFloat4 {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-12px) rotate(4deg); }
        }
        @keyframes heroFloat5 {
            0%, 100% { transform: translateY(0px) scale(1) rotate(0deg); }
            50% { transform: translateY(-15px) scale(1.08) rotate(10deg); }
        }
        @keyframes heroFloat6 {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-16px); }
        }

        /* Entrance animations */
        .hero-float-1 { animation-delay: 0s; opacity: 0; animation: heroFloat1 6s ease-in-out infinite, heroEntrance 0.8s ease-out 0.2s forwards; }
        .hero-float-2 { animation-delay: 0.1s; opacity: 0; animation: heroFloat2 5s ease-in-out infinite, heroEntrance 0.8s ease-out 0.4s forwards; }
        .hero-float-3 { animation-delay: 0.2s; opacity: 0; animation: heroFloat3 7s ease-in-out infinite, heroEntrance 0.8s ease-out 0.6s forwards; }
        .hero-float-4 { animation-delay: 0.3s; opacity: 0; animation: heroFloat4 5.5s ease-in-out infinite, heroEntrance 0.8s ease-out 0.8s forwards; }
        .hero-float-5 { animation-delay: 0.4s; opacity: 0; animation: heroFloat5 4s ease-in-out infinite, heroEntrance 0.8s ease-out 0.5s forwards; }
        .hero-float-6 { animation-delay: 0.5s; opacity: 0; animation: heroFloat6 6.5s ease-in-out infinite, heroEntrance 0.8s ease-out 0.3s forwards; }

        @keyframes heroEntrance {
            0% { opacity: 0; transform: translateY(40px) scale(0.8); }
            100% { opacity: 1; transform: translateY(0) scale(1); }
        }

        /* Hero text entrance */
        .hero h1 { opacity: 0; animation: heroTextSlide 1s ease-out 0.1s forwards; }
        .hero p { opacity: 0; animation: heroTextSlide 1s ease-out 0.3s forwards; }
        .hero div[style*="display: flex; gap: 1.5rem"] { opacity: 0; animation: heroTextSlide 1s ease-out 0.5s forwards; }

        @keyframes heroTextSlide {
            0% { opacity: 0; transform: translateX(-40px); }
            100% { opacity: 1; transform: translateX(0); }
        }
    </style>
'''

# Insert float CSS before the closing </head>
content = content.replace('</head>', float_css + '</head>')
print("2. Added floating + entrance animations ✓")

with open(file_path, 'w') as f:
    f.write(content)

print("\nAll hero upgrades applied!")
