# Question 2

Rank complexes based on the completeness of images using Postgre Query

## Explanation and Query

We have to create a view table with this query below. (notes : full query on the bottom of this README.md or see the [view_images_score.sql](https://github.com/jodiesamuel/test_spacestock/blob/master/question2/view_images_score.sql))
first thing we have to do is define the completeness of the images data. using "with" to define how much count of the data

```
with score as (
	select 
		c.id,
		coalesce(replace((images::json -> 'images_developer')::text,'"None"',null)::int,0) as images_developer,
		coalesce(replace((images::json -> 'images_banner')::text,'"None"',null)::int,0) as images_banner,
		coalesce(replace((images::json -> 'images_brochure')::text,'"None"',null)::int,0) as images_brochure,
		coalesce(ii.count_images_interior,0) as count_images_interior,
		coalesce(ie.count_images_exterior,0) as count_images_exterior,
		coalesce(i_360.count_images_360,0) as count_images_360 ,
		coalesce(replace((images::json -> 'video_link')::text,'"None"',null)::int,0) as video_link
	from 
		complex c 
	left join (
		select 
			id,
			count((images_interior::json -> 'url')::text)  as count_images_interior
		from (
			select id,
			jsonb_array_elements(case jsonb_typeof(images_interior) when 'array' then images_interior else '[]' end) images_interior
		from (select id,images::jsonb -> 'images_interior' as images_interior from complex) complex 
		) images_interior
		group by 1
	) ii on ii.id = c.id 
	left join (
		select 
			id,
			count((images_exterior::json -> 'url')::text)  as count_images_exterior
		from (
			select id,
			jsonb_array_elements(case jsonb_typeof(images_exterior) when 'array' then images_exterior else '[]' end) images_exterior
		from (select id,images::jsonb -> 'images_exterior' as images_exterior from complex) complex 
		) images_exterior
		group by 1
	) ie on ie.id = c.id 
	left join (
		select 
			id,
			count((images_360::json -> 'url')::text)  as count_images_360
		from (
			select id,
			jsonb_array_elements(case jsonb_typeof(images_360) when 'array' then images_360 else '[]' end) images_360
		from (select id,images::jsonb -> 'images_360' as images_360 from complex) complex 
		) images_360
		group by 1
	) i_360 on i_360.id = c.id 
)
```

![alt text](https://github.com/jodiesamuel/test_spacestock/blob/master/pictures/count_images.png)

after that count the score based on how much the completeness of the images data. 
![alt text](https://github.com/jodiesamuel/test_spacestock/blob/master/pictures/metric.png)
examples query based on metric from the question

```
case 
  when s.images_developer = 0 then 0
  when s.images_developer between 1 and 2 then 5
  when s.images_developer between 3 and 4 then 7
  when s.images_developer >= 5 then 10
end as images_developer_score
```

After that select all the columns that we need to create the view tables. To rank from the score we need to order it by descending and make a columns to total all of the score from all images.

```
(sc.images_developer_score + sc.images_banner_score + sc.images_brochure_score + 
sc.images_interior_score + sc.images_exterior_score + sc.images_360_score + sc.video_link_score) as total_score,
```

result : 

![alt text](https://github.com/jodiesamuel/test_spacestock/blob/master/pictures/view_images_score.png)

## Full query to create the view table
```
create view view_images_score as 	
with score as (
	select 
		c.id,
		coalesce(replace((images::json -> 'images_developer')::text,'"None"',null)::int,0) as images_developer,
		coalesce(replace((images::json -> 'images_banner')::text,'"None"',null)::int,0) as images_banner,
		coalesce(replace((images::json -> 'images_brochure')::text,'"None"',null)::int,0) as images_brochure,
		coalesce(ii.count_images_interior,0) as count_images_interior,
		coalesce(ie.count_images_exterior,0) as count_images_exterior,
		coalesce(i_360.count_images_360,0) as count_images_360 ,
		coalesce(replace((images::json -> 'video_link')::text,'"None"',null)::int,0) as video_link
	from 
		complex c 
	left join (
		select 
			id,
			count((images_interior::json -> 'url')::text)  as count_images_interior
		from (
			select id,
			jsonb_array_elements(case jsonb_typeof(images_interior) when 'array' then images_interior else '[]' end) images_interior
		from (select id,images::jsonb -> 'images_interior' as images_interior from complex) complex 
		) images_interior
		group by 1
	) ii on ii.id = c.id 
	left join (
		select 
			id,
			count((images_exterior::json -> 'url')::text)  as count_images_exterior
		from (
			select id,
			jsonb_array_elements(case jsonb_typeof(images_exterior) when 'array' then images_exterior else '[]' end) images_exterior
		from (select id,images::jsonb -> 'images_exterior' as images_exterior from complex) complex 
		) images_exterior
		group by 1
	) ie on ie.id = c.id 
	left join (
		select 
			id,
			count((images_360::json -> 'url')::text)  as count_images_360
		from (
			select id,
			jsonb_array_elements(case jsonb_typeof(images_360) when 'array' then images_360 else '[]' end) images_360
		from (select id,images::jsonb -> 'images_360' as images_360 from complex) complex 
		) images_360
		group by 1
	) i_360 on i_360.id = c.id 
)
select 
	sc.id,
	(sc.images_developer_score + sc.images_banner_score + sc.images_brochure_score + 
	sc.images_interior_score + sc.images_exterior_score + sc.images_360_score + sc.video_link_score) as total_score,
	c."name",
	c.developer_name as developer,
	c.address_province as province, 
	c.address_city as city,
	c.address_street as address,
	sc.images_developer_score,
	sc.images_banner_score,
	sc.images_brochure_score,
	sc.images_interior_score,
	sc.images_exterior_score,
	sc.images_360_score,
	sc.video_link_score
from (
	select 
		s.id,
		case 
			when s.images_developer = 0 then 0
			when s.images_developer between 1 and 2 then 5
			when s.images_developer between 3 and 4 then 7
			when s.images_developer >= 5 then 10
		end as images_developer_score,
		case 
			when s.images_banner = 0 then 0
			when s.images_banner between 1 and 2 then 10
			when s.images_banner between 3 and 4 then 10
			when s.images_banner >= 5 then 10
		end as images_banner_score,
		case 
			when s.images_brochure = 0 then 0
			when s.images_brochure between 1 and 2 then 7
			when s.images_brochure between 3 and 4 then 10
			when s.images_brochure >= 5 then 10
		end as images_brochure_score,
		case 
			when s.count_images_interior = 0 then 0
			when s.count_images_interior between 1 and 2 then 5
			when s.count_images_interior between 3 and 4 then 7
			when s.count_images_interior >= 5 then 10
		end as images_interior_score,
		case 
			when s.count_images_exterior = 0 then 0
			when s.count_images_exterior between 1 and 2 then 3
			when s.count_images_exterior between 3 and 4 then 5
			when s.count_images_exterior >= 5 then 10
		end as images_exterior_score,
		case 
			when s.count_images_360 = 0 then 0
			when s.count_images_360 between 1 and 2 then 7
			when s.count_images_360 between 3 and 4 then 10
			when s.count_images_360 >= 5 then 10
		end as images_360_score,
		case 
			when s.video_link = 0 then 0
			when s.video_link between 1 and 2 then 10
			when s.video_link between 3 and 4 then 10
			when s.video_link >= 5 then 10
		end as video_link_score
	from 
		score s 
) sc 
left join 
	complex c on c.id = sc.id
order by 
	total_score desc
```
