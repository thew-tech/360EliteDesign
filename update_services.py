import sys, re

file_path = '/home/ali/Music/360EliteDesign.com/index.html'

try:
    with open(file_path, 'r') as f:
        content = f.read()

    new_services = """<!-- 3D Flipping Photo Cards Services Section -->
    <section class="services relative overflow-hidden" id="services" style="background-color: #f8fafc; padding: 120px 0;">
        <div class="container mx-auto px-6 relative z-10 max-w-[1400px]">
            <div class="text-center mb-24 scroll-reveal">
                <h4 class="text-blue-600 font-bold tracking-widest uppercase mb-4 text-sm">Our Expertise</h4>
                <h2 class="text-slate-900 text-5xl md:text-6xl font-extrabold font-['Outfit'] mb-6 leading-tight">Comprehensive Digital Solutions</h2>
                <p class="text-slate-500 text-xl max-w-2xl mx-auto leading-relaxed">We deliver high-end, scalable, and visually stunning digital products that accelerate your business growth.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10" style="perspective: 1500px;">
                <!-- Service 1: Web Design -->
                <div class="flip-card scroll-reveal stagger-1 h-[450px]">
                    <div class="flip-card-inner">
                        <div class="flip-card-front" style="background-image: url('https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=800&auto=format&fit=crop');">
                            <div class="overlay"></div>
                            <div class="front-content">
                                <i class="ph-bold ph-desktop text-6xl text-blue-400 mb-4 drop-shadow-lg"></i>
                                <h3 class="text-3xl font-bold text-white font-['Outfit']">Web Design</h3>
                            </div>
                        </div>
                        <div class="flip-card-back bg-gradient-to-br from-blue-700 to-cyan-500">
                            <i class="ph-bold ph-desktop text-5xl text-white/50 mb-6"></i>
                            <h3 class="text-2xl font-bold text-white mb-4 font-['Outfit']">Web Design & Development</h3>
                            <p class="text-white/90 text-lg leading-relaxed">Custom, high-performance websites built with the latest technologies to engage and convert your audience instantly.</p>
                        </div>
                    </div>
                </div>

                <!-- Service 2: UI/UX -->
                <div class="flip-card scroll-reveal stagger-2 h-[450px]">
                    <div class="flip-card-inner">
                        <div class="flip-card-front" style="background-image: url('https://images.unsplash.com/photo-1561070791-2526d30994b5?q=80&w=800&auto=format&fit=crop');">
                            <div class="overlay"></div>
                            <div class="front-content">
                                <i class="ph-bold ph-bezier-curve text-6xl text-blue-400 mb-4 drop-shadow-lg"></i>
                                <h3 class="text-3xl font-bold text-white font-['Outfit']">UI/UX Design</h3>
                            </div>
                        </div>
                        <div class="flip-card-back bg-gradient-to-br from-blue-700 to-cyan-500">
                            <i class="ph-bold ph-bezier-curve text-5xl text-white/50 mb-6"></i>
                            <h3 class="text-2xl font-bold text-white mb-4 font-['Outfit']">UI/UX Design</h3>
                            <p class="text-white/90 text-lg leading-relaxed">Intuitive, user-centered interfaces providing seamless and memorable experiences across all devices.</p>
                        </div>
                    </div>
                </div>

                <!-- Service 3: Branding -->
                <div class="flip-card scroll-reveal stagger-3 h-[450px]">
                    <div class="flip-card-inner">
                        <div class="flip-card-front" style="background-image: url('https://images.unsplash.com/photo-1600132806370-bf17e65e942f?q=80&w=800&auto=format&fit=crop');">
                            <div class="overlay"></div>
                            <div class="front-content">
                                <i class="ph-bold ph-pen-nib text-6xl text-blue-400 mb-4 drop-shadow-lg"></i>
                                <h3 class="text-3xl font-bold text-white font-['Outfit']">Brand Identity</h3>
                            </div>
                        </div>
                        <div class="flip-card-back bg-gradient-to-br from-blue-700 to-cyan-500">
                            <i class="ph-bold ph-pen-nib text-5xl text-white/50 mb-6"></i>
                            <h3 class="text-2xl font-bold text-white mb-4 font-['Outfit']">Brand Identity</h3>
                            <p class="text-white/90 text-lg leading-relaxed">Memorable logos and cohesive brand guidelines that make your business stand out powerfully from the competition.</p>
                        </div>
                    </div>
                </div>

                <!-- Service 4: E-commerce -->
                <div class="flip-card scroll-reveal stagger-1 h-[450px]">
                    <div class="flip-card-inner">
                        <div class="flip-card-front" style="background-image: url('https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?q=80&w=800&auto=format&fit=crop');">
                            <div class="overlay"></div>
                            <div class="front-content">
                                <i class="ph-bold ph-shopping-cart text-6xl text-blue-400 mb-4 drop-shadow-lg"></i>
                                <h3 class="text-3xl font-bold text-white font-['Outfit']">E-commerce</h3>
                            </div>
                        </div>
                        <div class="flip-card-back bg-gradient-to-br from-blue-700 to-cyan-500">
                            <i class="ph-bold ph-shopping-cart text-5xl text-white/50 mb-6"></i>
                            <h3 class="text-2xl font-bold text-white mb-4 font-['Outfit']">E-commerce Solutions</h3>
                            <p class="text-white/90 text-lg leading-relaxed">Scalable online stores designed to maximize sales, streamline operations, and deeply enhance customer loyalty.</p>
                        </div>
                    </div>
                </div>

                <!-- Service 5: Marketing -->
                <div class="flip-card scroll-reveal stagger-2 h-[450px]">
                    <div class="flip-card-inner">
                        <div class="flip-card-front" style="background-image: url('https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800&auto=format&fit=crop');">
                            <div class="overlay"></div>
                            <div class="front-content">
                                <i class="ph-bold ph-trend-up text-6xl text-blue-400 mb-4 drop-shadow-lg"></i>
                                <h3 class="text-3xl font-bold text-white font-['Outfit']">Digital Marketing</h3>
                            </div>
                        </div>
                        <div class="flip-card-back bg-gradient-to-br from-blue-700 to-cyan-500">
                            <i class="ph-bold ph-trend-up text-5xl text-white/50 mb-6"></i>
                            <h3 class="text-2xl font-bold text-white mb-4 font-['Outfit']">Digital Marketing & SEO</h3>
                            <p class="text-white/90 text-lg leading-relaxed">Data-driven strategies to increase visibility, drive targeted traffic, and predictably accelerate business growth.</p>
                        </div>
                    </div>
                </div>

                <!-- Service 6: Mobile Apps -->
                <div class="flip-card scroll-reveal stagger-3 h-[450px]">
                    <div class="flip-card-inner">
                        <div class="flip-card-front" style="background-image: url('https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?q=80&w=800&auto=format&fit=crop');">
                            <div class="overlay"></div>
                            <div class="front-content">
                                <i class="ph-bold ph-device-mobile text-6xl text-blue-400 mb-4 drop-shadow-lg"></i>
                                <h3 class="text-3xl font-bold text-white font-['Outfit']">Mobile Apps</h3>
                            </div>
                        </div>
                        <div class="flip-card-back bg-gradient-to-br from-blue-700 to-cyan-500">
                            <i class="ph-bold ph-device-mobile text-5xl text-white/50 mb-6"></i>
                            <h3 class="text-2xl font-bold text-white mb-4 font-['Outfit']">Mobile App Design</h3>
                            <p class="text-white/90 text-lg leading-relaxed">Engaging native and cross-platform mobile applications tailored precisely for optimal user retention.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 3D Flip Card CSS & Scroll Logic -->
    <style>
        .flip-card {
            background-color: transparent;
            perspective: 1500px;
            cursor: pointer;
        }
        
        .flip-card-inner {
            position: relative;
            width: 100%;
            height: 100%;
            text-align: center;
            transition: transform 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            transform-style: preserve-3d;
            border-radius: 28px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        }

        .flip-card:hover .flip-card-inner {
            transform: rotateY(180deg) scale(1.05); /* Flips and lifts toward user */
            box-shadow: 0 30px 60px rgba(0, 123, 255, 0.4);
        }

        .flip-card-front, .flip-card-back {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            -webkit-backface-visibility: hidden;
            backface-visibility: hidden;
            border-radius: 28px;
            overflow: hidden;
        }

        .flip-card-front {
            background-size: cover;
            background-position: center;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
        }

        .flip-card-front .overlay {
            position: absolute;
            inset: 0;
            background: linear-gradient(to top, rgba(10,25,47,0.95), rgba(10,25,47,0.2));
            z-index: 1;
            transition: opacity 0.4s ease;
        }
        
        .flip-card:hover .flip-card-front .overlay {
            opacity: 0.4;
        }

        .flip-card-front .front-content {
            position: relative;
            z-index: 2;
            transform: translateZ(60px); /* 3D depth effect */
            transition: transform 0.4s ease;
        }

        .flip-card-back {
            color: white;
            transform: rotateY(180deg);
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            padding: 40px;
        }
        
        /* Scroll Reveal Animation Classes */
        .scroll-reveal { opacity: 0; transform: translateY(60px); transition: all 1s cubic-bezier(0.2, 0.8, 0.2, 1); }
        .scroll-reveal.visible { opacity: 1; transform: translateY(0); }
        .stagger-1 { transition-delay: 0.1s; } .stagger-2 { transition-delay: 0.25s; } .stagger-3 { transition-delay: 0.4s; }
    </style>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                    }
                });
            }, { threshold: 0.1, rootMargin: "0px 0px -50px 0px" });

            document.querySelectorAll('.scroll-reveal').forEach(el => observer.observe(el));
        });
    </script>"""

    start_str = "<!-- Premium Redesigned Services Section -->"
    end_str = "</script>"
    start_idx = content.find(start_str)
    
    # If the user hasn't pasted the Premium Redesigned block, fall back to replacing the old block.
    if start_idx == -1:
        start_str = "<!-- Services Section -->"
        start_idx = content.find(start_str)
        # For the old block, the end is </section>
        end_str = "</section>"

    if start_idx != -1:
        end_idx = content.find(end_str, start_idx)
        if end_idx != -1:
            end_idx += len(end_str)
            content = content[:start_idx] + new_services + content[end_idx:]
            with open(file_path, 'w') as f:
                f.write(content)
            print("Successfully injected 3D flipping photo cards directly into index.html!")
        else:
            print("Could not find the end of the services section.")
    else:
        print("Could not find the start of the services section.")

except Exception as e:
    print(e)
