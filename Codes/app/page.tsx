'use client';

import { motion } from 'framer-motion';
import Navbar from '@/components/Navbar';
import Footer from '@/components/Footer';
import Link from 'next/link';

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-900 text-white font-sans">
      <Navbar />

      {/* Hero Section */}
      <section className="h-screen flex flex-col items-center justify-center text-center p-10">
        <motion.h1
          className="text-6xl font-bold max-w-4xl"
          initial={{ opacity: 0, y: -50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1 }}
        >
          AI-Driven Content Personalization for Maximum Engagement
        </motion.h1>
        <motion.p
          className="text-lg mt-4 max-w-2xl"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.5, duration: 1 }}
        >
          Unlock the power of AI to create compelling, data-driven marketing
          campaigns tailored for your audience.
        </motion.p>
        <Link href="/contact">
          <motion.button
            className="mt-6 px-6 py-3 bg-blue-600 text-white rounded-lg text-lg hover:bg-blue-700 transition"
            whileHover={{ scale: 1.1 }}
          >
            Get Started
          </motion.button>
        </Link>
      </section>

      {/* Services Section */}
      <section className="py-20 px-10 bg-gray-800">
        <h2 className="text-4xl font-semibold text-center mb-10">
          Our Services
        </h2>
        <div className="grid md:grid-cols-3 gap-8">
          {[
            'AI Content Optimization',
            'Personalized Messaging',
            'Data-Driven Insights',
            'Automated A/B Testing',
            'Predictive Analytics',
            'Brand Voice Customization',
            'Real-Time Performance Analysis',
            'Customer Journey Mapping',
            'Multi-Channel AI Integration',
          ].map((service, index) => (
            <motion.div
              key={index}
              className="p-6 bg-gray-700 rounded-xl shadow-lg hover:shadow-2xl transition"
              whileHover={{ scale: 1.05 }}
            >
              <h3 className="text-2xl font-medium">{service}</h3>
              <p className="mt-2 text-gray-300">
                Harness AI to enhance your marketing efforts and maximize ROI.
              </p>
            </motion.div>
          ))}
        </div>
      </section>

      {/* Case Studies Section */}
      <section className="py-20 px-10 bg-gray-900">
        <h2 className="text-4xl font-semibold text-center mb-10">
          Success Stories
        </h2>
        <div className="grid md:grid-cols-3 gap-8">
          {[
            'Fortune 500 Brand Growth',
            'E-Commerce AI Boost',
            'SaaS Retention Strategy',
            'Retail Consumer Behavior Insights',
            'Healthcare AI-Powered Campaigns',
          ].map((caseStudy, index) => (
            <motion.div
              key={index}
              className="p-6 bg-gray-800 rounded-xl shadow-lg hover:shadow-2xl transition"
              whileHover={{ scale: 1.05 }}
            >
              <h3 className="text-2xl font-medium">{caseStudy}</h3>
              <p className="mt-2 text-gray-300">
                Discover how AI-driven insights transformed marketing
                strategies.
              </p>
              <Link
                href="/case-studies"
                className="text-blue-500 mt-4 block hover:underline"
              >
                Read More
              </Link>
            </motion.div>
          ))}
        </div>
      </section>

      {/* AI-powered Insights Section */}
      <section className="py-20 px-10 bg-gray-800">
        <h2 className="text-4xl font-semibold text-center mb-10">
          How AI Works
        </h2>
        <p className="text-center max-w-2xl mx-auto text-gray-300 mb-6">
          Our AI analyzes millions of customer interactions to craft the most
          effective marketing messages, driving higher engagement and
          conversions.
        </p>
        <div className="grid md:grid-cols-3 gap-8">
          {[
            'Deep Learning Models',
            'Behavioral Predictive Analysis',
            'Adaptive Content Generation',
          ].map((feature, index) => (
            <motion.div
              key={index}
              className="p-6 bg-gray-700 rounded-xl shadow-lg hover:shadow-2xl transition"
              whileHover={{ scale: 1.05 }}
            >
              <h3 className="text-2xl font-medium">{feature}</h3>
              <p className="mt-2 text-gray-300">
                Our AI dynamically adjusts marketing campaigns based on
                real-time audience responses.
              </p>
            </motion.div>
          ))}
        </div>
      </section>

      {/* Contact CTA */}
      <section className="py-20 px-10 bg-blue-700 text-center text-white">
        <h2 className="text-4xl font-semibold">
          Ready to Revolutionize Your Marketing?
        </h2>
        <p className="text-lg mt-4">
          Let AI take your brand to the next level.
        </p>
        <Link href="/contact">
          <motion.button
            className="mt-6 px-6 py-3 bg-white text-blue-700 rounded-lg text-lg hover:bg-gray-200 transition"
            whileHover={{ scale: 1.1 }}
          >
            Contact Us
          </motion.button>
        </Link>
      </section>

      <Footer />
    </div>
  );
}
