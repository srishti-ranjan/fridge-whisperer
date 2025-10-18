# fridge-whisperer
Smart Grocery List
Fridge Whisperer is a scalable smart fridge management system built with Python microservices, Docker, and Kubernetes. It helps users track inventory, get personalized recommendations, and receive timely notifications.

Microservices Include
1. **PantryPal** covers core inventory management for all items, supporting searches and tracking physical stock.​
2. **UseLogix** enables data-driven insights into usage, allowing for predictive restocking and consumption analysis.​
3. **SmartSuggest** uses data from PantryPal and UseLogix to drive shopping and recipe recommendations, enhancing user value.​
4. **PingMe** ensures operational responsiveness, keeping users informed about their inventory status without manual checks.​
5. **TasteTune** holds and applies the user's dietary information and taste profiles, ensuring personal relevance in all outputs.
