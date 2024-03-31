from src.pages import Landing, Login, Dashboard, Explore, Profile,EditDeck, AddCard, Changedeck

ROUTES = {
    "/landing": Landing.LandingPage,
    "/login": Login.LoginPage,
    "/": Dashboard.DashboardPage,
    "/explore": Explore.ExplorePage,
    "/profile": Profile.ProfilePage,
    "/edit": EditDeck.EditDeckPage,
    "/add-card": AddCard.AddCardPage,
    "/changedeck": Changedeck.ChangedeckPage,
}