from src.pages import Landing, Login, Dashboard, Explore, Profile

ROUTES = {
    "/landing": Landing.LandingPage,
    "/login": Login.LoginPage,
    "/": Dashboard.DashboardPage,
    "/explore": Explore.ExplorePage,
    "/profile": Profile.ProfilePage,
}