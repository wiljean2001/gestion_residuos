import { cn } from '@lib/utils'
import { useStore } from '@nanostores/react';
import { sidebar } from '@stores/sidebar/sidebarStore';


export default function Footer() {
	const { isOpen } = useStore(sidebar);

	return (
		<footer
			className={cn(
				"transition-[margin-left] ease-in-out duration-300",
				isOpen === false ? "lg:ml-[90px]" : "lg:ml-72"
			)}
		>
			<div
				className="supports-backdrop-blur:bg-background/60 z-20 w-full shadow bg-background/95 backdrop-blur"
			>
				<div className="mx-4 md:mx-8 flex h-14 items-center">
					<p className="text-xs md:text-sm leading-loose text-muted-foreground text-left">
						Sistema de gestion de residuos sólidos peligrosos, no peligrosos y RAEEs. © 2024{" "}
						{/* <a
							href="https://ui.shadcn.com"
							target="_blank"
							rel="noopener noreferrer"
							className="font-medium underline underline-offset-4"
						>
							shadcn/ui
						</a> */}
						. Todos los derechos reservados {" "}
						{/* <a
							href="https://github.com/salimi-my/shadcn-ui-sidebar"
							target="_blank"
							rel="noopener noreferrer"
							className="font-medium underline underline-offset-4"
						>
							GitHub
						</a> */}
						.
					</p>
				</div>
			</div>
		</footer>


	)
}