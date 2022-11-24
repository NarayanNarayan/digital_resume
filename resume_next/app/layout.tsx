/* eslint-disable @next/next/no-head-element */
'use client';
import Link from 'next/link';
import './globals.css';
import Navbar from './navbar';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html>
      <head></head>
      <body>
        <Navbar></Navbar>
        {children}
      </body>
    </html>
  );
}
