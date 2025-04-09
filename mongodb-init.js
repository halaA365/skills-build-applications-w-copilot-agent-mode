use monafit_db;

// Create collections
db.createCollection("users");
db.createCollection("teams");
db.createCollection("activities");
db.createCollection("leaderboard");
db.createCollection("workouts");

// Ensure unique email for users
db.users.createIndex({ "email": 1 }, { unique: true });
