if pcall(require, 'graphite') then
	print "Module has been loaded successfully."
else
	print "Some error happen."
	os.exit(1)
end
