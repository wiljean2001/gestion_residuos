import { cn } from '@lib/utils'
import React from 'react'

import { useStore } from '@nanostores/react';
import { sidebar } from '@stores/sidebar/sidebarStore';

interface MainProps {
    children: React.ReactNode
}
export default function Main({ children }: MainProps) {
    const { isOpen } = useStore(sidebar);
    return (
        <main
            className={cn(
                "min-h-[calc(100vh_-_56px)] bg-zinc-50 dark:bg-zinc-900 transition-[margin-left] ease-in-out duration-300",
                isOpen === false ? "lg:ml-[90px]" : "lg:ml-72"
            )}
        >
            {children}
        </main>

    )
}
