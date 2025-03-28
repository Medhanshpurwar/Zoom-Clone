import { clerkMiddleware, createRouteMatcher } from "@clerk/nextjs/server";
import { NextResponse } from "next/server";

// ✅ Define protected routes using createRouteMatcher
const isProtectedRoute = createRouteMatcher([
  "/",
  "/upcoming",
  "/previous",
  "/recordings",
  "/personal-room",
  "/meeting(.*)", // ✅ Regex pattern for dynamic routes
]);

// ✅ Clerk Middleware to handle protected routes
export default clerkMiddleware(async (auth, req) => {
  // ✅ Check if the requested route is protected
  if (isProtectedRoute(req)) {
    // ✅ Authenticate and protect the route manually
    const { userId } = await auth();

    // ✅ Check if user is authenticated
    if (!userId) {
        return NextResponse.redirect(new URL("/sign-in", req.url));
    }
  }

  // ✅ Allow access to unprotected routes
  return NextResponse.next();
});

// ✅ Define the matcher to apply middleware to specific routes
export const config = {
  matcher: [
    "/((?!.+\\.[\\w]+$|_next).*)", // Matches all routes except static files and _next
    "/",                          // Root route
    "/(api|trpc)(.*)",            // API and TRPC routes
  ],
};
