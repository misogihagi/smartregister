import replace from 'rollup-plugin-replace';

export default {
	input: 'src/main.js',
	plugins: [
		replace({ 'process.browser': !!process.env.BROWSER })
	],
	output: {
		sourcemap: true,
		format: 'iife',
		name: 'Bandoor',
		file: `build/bundle.${process.env.BROWSER ? 'browser' : 'node'}.js`
	},
	watch: {
		clearScreen: false
	}
};

