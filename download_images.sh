#!/bin/bash
cd /home/ali/Music/360EliteDesign.com/images

echo "Downloading hero background..."
curl -sL -o hero-team.jpg "https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=2670&auto=format&fit=crop"
echo "Done: hero-team.jpg"

echo "Downloading web-design card..."
curl -sL -o service-webdesign.jpg "https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=800&auto=format&fit=crop"
echo "Done: service-webdesign.jpg"

echo "Downloading uiux card..."
curl -sL -o service-uiux.jpg "https://images.unsplash.com/photo-1561070791-2526d30994b5?q=80&w=800&auto=format&fit=crop"
echo "Done: service-uiux.jpg"

echo "Downloading branding card..."
curl -sL -o service-branding.jpg "https://images.unsplash.com/photo-1600132806370-bf17e65e942f?q=80&w=800&auto=format&fit=crop"
echo "Done: service-branding.jpg"

echo "Downloading ecommerce card..."
curl -sL -o service-ecommerce.jpg "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?q=80&w=800&auto=format&fit=crop"
echo "Done: service-ecommerce.jpg"

echo "Downloading marketing card..."
curl -sL -o service-marketing.jpg "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800&auto=format&fit=crop"
echo "Done: service-marketing.jpg"

echo "Downloading mobile app card..."
curl -sL -o service-mobileapp.jpg "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?q=80&w=800&auto=format&fit=crop"
echo "Done: service-mobileapp.jpg"

echo "Downloading portfolio webdesign large..."
curl -sL -o portfolio-webdesign.jpg "https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=2072&auto=format&fit=crop"
echo "Done: portfolio-webdesign.jpg"

echo "Downloading portfolio branding large..."
curl -sL -o portfolio-branding.jpg "https://images.unsplash.com/photo-1600132806370-bf17e65e942f?q=80&w=2194&auto=format&fit=crop"
echo "Done: portfolio-branding.jpg"

echo ""
echo "All images downloaded!"
ls -lh /home/ali/Music/360EliteDesign.com/images/
