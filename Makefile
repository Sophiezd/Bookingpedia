# Launch Website
start: ; docker-compose build ; docker-compose up
# Close Website
close: ; docker-compose down
# Restart Website
restart: ; docker-compose down ; docker-compose build ; docker-compose up
# Remove local database
clean: ; docker-compose down ; docker volume rm bookingpedia_postgres_data