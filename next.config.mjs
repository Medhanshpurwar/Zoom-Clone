// next.config.mjs

import dotenv from 'dotenv';
dotenv.config();

/** @type {import('next').NextConfig} */
const nextConfig = {
  env: {
    NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY: process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY,
    CLERK_SECRET_KEY: process.env.CLERK_SECRET_KEY,
    NEXT_PUBLIC_CLERK_SIGN_IN_URL: process.env.NEXT_PUBLIC_CLERK_SIGN_IN_URL,
    NEXT_PUBLIC_CLERK_SIGN_UP_URL: process.env.NEXT_PUBLIC_CLERK_SIGN_UP_URL,
    NEXT_PUBLIC_STREAM_API_KEY: process.env.NEXT_PUBLIC_STREAM_API_KEY,
    STREAM_SECRET_KEY: process.env.STREAM_SECRET_KEY,
  },
  reactStrictMode: true,
  webpack(config) {
    config.output.hashSalt = 'custom-salt'; // ✅ Add this line
    return config;
  },
};

console.log('✅ Clerk Publishable Key:', process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY);
console.log('✅ Stream API Key:', process.env.NEXT_PUBLIC_STREAM_API_KEY);

export default nextConfig;
