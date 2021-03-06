#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  db_concepts.py
#  
#  Copyright 2017 Austin <theganoush@Eggplant-Pi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import imdb


def main(args):
	movie_access = imdb.IMDb(accessSystem = 'http')
	movie_list = movie_access.get_top250_movies()
	
	movie_access.update(movie_list[0])
	print movie_list[0].summary()
	
	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
