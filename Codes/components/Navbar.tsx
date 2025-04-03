import Link from 'next/link';

export default function Navbar() {
  return (
    <nav className="p-4 bg-gray-800 flex justify-between items-center text-white">
      <div className="text-2xl font-bold">My AI Platform</div>
      <ul className="flex gap-6">
        <li>
          <Link href="/" className="hover:text-blue-400">
            Home
          </Link>
        </li>
        <li>
          <Link href="/about" className="hover:text-blue-400">
            About
          </Link>
        </li>
        <li>
          <Link href="/products" className="hover:text-blue-400">
            Products
          </Link>
        </li>
        <li>
          <Link href="/industries" className="hover:text-blue-400">
            Industries
          </Link>
        </li>
        <li>
          <Link href="/contact" className="hover:text-blue-400">
            Contact
          </Link>
        </li>
      </ul>
    </nav>
  );
}
