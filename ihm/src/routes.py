from src.pages import Landing, Login, Dashboard

ROUTES = {
    "/landing": Landing.LandingPage,
    "/login": Login.LoginPage,
    "/": Dashboard.DashboardPage,
}