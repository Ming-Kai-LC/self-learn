# Data Engineering Intermediate - Real-Time Streaming
> Master real-time data streaming and event-driven architectures with Apache Kafka and Flink

## About This Project

This intermediate-level course builds on data engineering fundamentals to teach you how to build production-grade real-time streaming systems. Through hands-on projects, you'll learn to process continuous data streams, handle events at scale, and implement event-driven architectures using open-source tools.

This course focuses on **practical streaming skills** that power modern applications:
- Processing millions of events per second
- Real-time analytics and monitoring
- Event-driven microservices
- Stateful stream processing
- Exactly-once processing guarantees

Whether you're scaling from batch ETL to real-time pipelines, building event-driven systems, or adding streaming capabilities to your data platform, this course provides the essential knowledge and hands-on experience.

**Prerequisites**: This course builds on data engineering fundamentals. You should be comfortable with Python, basic ETL concepts, and data processing with pandas.

## Who This Is For

This learning path is designed for:

- **Data Engineers** transitioning from batch to streaming pipelines
- **Backend Engineers** building event-driven systems
- **Data Scientists** needing real-time feature engineering
- **Software Engineers** working with distributed systems
- **Anyone** who completed the Data Engineering Fundamentals course

### Prerequisites Knowledge Level
- **Intermediate Python**: Comfortable with classes, async/await, context managers
- **Basic ETL**: Understanding of extract, transform, load patterns
- **SQL and data modeling**: JOIN operations, schema design
- **Command line proficiency**: Basic Docker usage helpful
- **Completed Data Engineering Fundamentals** or equivalent knowledge

## What You'll Learn

By completing this course, you will:

### Core Streaming Concepts
- Event streaming vs batch processing
- Event-driven architecture patterns
- Stream processing semantics (at-most-once, at-least-once, exactly-once)
- Stateful vs stateless processing
- Windowing strategies (tumbling, sliding, session)

### Apache Kafka Mastery
- Kafka architecture (brokers, topics, partitions)
- Producers and consumers
- Consumer groups and partition assignment
- Kafka Connect for data integration
- Schema Registry and data formats

### Apache Flink Fundamentals
- Flink DataStream API
- Transformations and operations
- Joins (stream-stream, stream-table)
- Watermarks and event time processing
- State management and checkpointing

### Production Patterns
- Exactly-once processing guarantees
- Fault tolerance and checkpointing
- Stateful stream processing
- Window-based aggregations
- Stream joins and correlations

## Project Structure

```
data-engineering-intermediate-streaming/
│
├── README.md                          # This file - comprehensive project guide
├── requirements.txt                   # Python dependencies for streaming
├── docker-compose.yml                 # Local Kafka + Flink cluster setup
│
├── notebooks/                         # Jupyter notebooks for learning
│   ├── 00_setup_introduction.ipynb                    # Setup and streaming intro (30 min)
│   ├── 01_introduction_to_event_streaming.ipynb       # Event streaming concepts (60 min)
│   ├── 02_kafka_deep_dive.ipynb                       # Kafka architecture (75 min)
│   ├── 03_stream_processing_fundamentals.ipynb        # Stream processing basics (60 min)
│   ├── 04_apache_flink_basics.ipynb                   # Flink DataStream API (75 min)
│   ├── 05_advanced_stream_processing.ipynb            # Joins, watermarks (75 min)
│   ├── 06_state_management_checkpointing.ipynb        # Stateful streams (60 min)
│   └── outputs/                       # Generated files and artifacts
│
├── data/                              # Sample data and streams
│   ├── raw/                          # Source data files
│   ├── streams/                      # Event stream data
│   ├── checkpoints/                  # Flink checkpoints
│   └── .gitkeep
│
├── configs/                           # Configuration files
│   ├── kafka/                        # Kafka configurations
│   ├── flink/                        # Flink configurations
│   └── .gitkeep
│
└── scripts/                           # Utility scripts
    ├── setup_helpers.py              # Environment verification
    ├── fix_emojis.py                 # Windows compatibility
    ├── start_kafka.sh                # Start Kafka cluster
    ├── start_flink.sh                # Start Flink cluster
    └── generate_events.py            # Event data generator
```

## Prerequisites

### Required Software

1. **Python 3.8 or higher**
   - Download from: https://www.python.org/downloads/
   - Verify installation: `python --version`

2. **Docker Desktop**
   - Download from: https://www.docker.com/products/docker-desktop
   - Required for running Kafka and Flink locally
   - Verify: `docker --version` and `docker-compose --version`

3. **Jupyter Notebook or JupyterLab**
   - Will be installed via requirements.txt
   - Alternative: Use VS Code with Jupyter extension

4. **Git** (for cloning the repository)
   - Download from: https://git-scm.com/

### Optional but Recommended

- **Kafka CLI Tools** (included in Docker images)
- **kafkacat/kcat** (for debugging Kafka)
- **VS Code** with Python and Jupyter extensions
- **DBeaver** or similar SQL client (for viewing results)

### System Requirements
- **RAM**: 8GB minimum, 16GB+ recommended (for Docker containers)
- **Disk Space**: 10GB for Docker images and data
- **OS**: Windows 10/11, macOS 10.15+, or Linux
- **CPU**: 4+ cores recommended for running clusters

### Knowledge Prerequisites

**You should understand** (from Data Engineering Fundamentals):
- ETL pipeline concepts (Module 01)
- Data extraction and transformation (Modules 02-03)
- Data quality and validation (Module 08)
- Pipeline design patterns (Module 05)

**Not required but helpful**:
- Distributed systems concepts
- Message queues basics
- Docker and containerization

## Installation

Follow these steps to set up your streaming environment:

### Step 1: Clone or Navigate to the Repository

```bash
# If you haven't cloned the portfolio yet
git clone https://github.com/yourusername/python-projects-portfolio.git
cd python-projects-portfolio/projects/data-engineering-intermediate-streaming

# If you already have the portfolio
cd python-projects-portfolio/projects/data-engineering-intermediate-streaming
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Python Dependencies

```bash
# Install all required packages
pip install -r requirements.txt

# Verify installation
python -c "import kafka, pyflink; print('Streaming libraries installed successfully!')"
```

### Step 4: Start Docker Containers

```bash
# Start Kafka and Flink clusters
docker-compose up -d

# Verify services are running
docker-compose ps

# Check logs
docker-compose logs kafka
docker-compose logs flink-jobmanager
```

You should see:
- Kafka broker running on localhost:9092
- Flink JobManager UI on http://localhost:8081
- ZooKeeper running on localhost:2181

### Step 5: Launch Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook

# Or start JupyterLab (recommended)
jupyter lab
```

Your browser should open automatically to the Jupyter interface. Navigate to the `notebooks/` folder and start with `00_setup_introduction.ipynb`.

### Step 6: Verify Setup

Open and run `00_setup_introduction.ipynb` to:
- Verify all dependencies are installed correctly
- Test Kafka connection
- Test Flink connection
- Run your first streaming example

## Learning Path

This course is designed to be followed sequentially. Each module builds upon concepts from previous modules.

### Module 00: Setup and Introduction to Streaming (30 minutes)
**File**: `00_setup_introduction.ipynb`

- Verify environment setup (Python, Docker, Kafka, Flink)
- Streaming vs batch processing comparison
- Overview of real-time data processing landscape
- Your first streaming "Hello World" example
- Understanding event time vs processing time

**Key Takeaway**: Environment is ready and you understand core streaming concepts.

---

### Module 01: Introduction to Event Streaming (60 minutes)
**File**: `01_introduction_to_event_streaming.ipynb`

- Event-driven architecture principles
- Apache Kafka fundamentals
  - Brokers, topics, and partitions
  - Producers and consumers
  - Consumer groups
- Setting up local Kafka cluster
- Producing and consuming first events
- Kafka use cases in industry

**Key Takeaway**: Understand Kafka's role in modern data architectures.

**Mini-Project**: Build a simple event producer/consumer pair

---

### Module 02: Kafka Deep Dive (75 minutes)
**File**: `02_kafka_deep_dive.ipynb`

- Kafka architecture in depth
  - Partitioning strategies
  - Replication and fault tolerance
  - Log compaction
- Consumer group coordination
- Offset management
- Kafka Connect for data integration
- Schema Registry and Avro

**Key Takeaway**: Master Kafka's distributed architecture and configuration.

**Mini-Project**: Implement a multi-partition producer with consumer groups

---

### Module 03: Stream Processing Fundamentals (60 minutes)
**File**: `03_stream_processing_fundamentals.ipynb`

- Stream processing concepts
- Stateless vs stateful operations
- Windowing patterns
  - Tumbling windows
  - Sliding windows
  - Session windows
- Aggregations over streams
- Time semantics (event time, processing time, ingestion time)

**Key Takeaway**: Understand fundamental stream processing patterns.

**Mini-Project**: Real-time analytics with windowed aggregations

---

### Module 04: Apache Flink Basics (75 minutes)
**File**: `04_apache_flink_basics.ipynb`

- Introduction to Apache Flink
- Flink architecture (JobManager, TaskManagers)
- DataStream API basics
- Transformations (map, filter, flatMap)
- KeyedStreams and reduce operations
- Writing your first Flink job

**Key Takeaway**: Build and deploy Flink streaming applications.

**Mini-Project**: Flink streaming job with transformations

---

### Module 05: Advanced Stream Processing (75 minutes)
**File**: `05_advanced_stream_processing.ipynb`

- Stream joins
  - Window joins
  - Interval joins
- Stream-table joins
- Watermarks and late data handling
- Allowed lateness
- Side outputs for late events

**Key Takeaway**: Handle complex stream processing scenarios.

**Mini-Project**: Multi-stream correlation with joins

---

### Module 06: State Management and Checkpointing (60 minutes)
**File**: `06_state_management_checkpointing.ipynb`

- State in stream processing
- Flink state backends (memory, RocksDB)
- Stateful operations (reduce, aggregate)
- Checkpointing for fault tolerance
- Savepoints for versioning
- Exactly-once processing guarantees

**Key Takeaway**: Build fault-tolerant stateful streaming applications.

**Mini-Project**: Stateful aggregations with checkpointing

---

### Total Estimated Time: 7-8 hours

## Future Modules (Planned)

The following advanced modules are planned for future development:

- **Module 07**: Stream Processing Patterns (CDC, Event Sourcing, CQRS)
- **Module 08**: Monitoring and Operations (Metrics, debugging, performance tuning)
- **Module 09**: Capstone Project (Complete real-time e-commerce platform)

**Current Focus**: The 7 existing modules (00-06) provide comprehensive coverage of Kafka and Flink fundamentals, preparing you for production streaming systems. The planned modules will add advanced production patterns and a complete capstone project.

## How to Use This Project

### Recommended Approach

1. **Follow sequentially**: Start with Module 00 and progress in order
2. **Docker first**: Ensure Docker containers are running before starting
3. **Hands-on practice**: Run every code cell, don't just read
4. **Mini-projects**: Complete each mini-project before moving on
5. **Experiment**: Modify parameters, break things, learn by doing
6. **Build portfolio**: Save your mini-project variations

### For Each Module

1. **Read the introduction**: Understand the module objectives
2. **Start Docker services**: Ensure Kafka/Flink are running
3. **Follow along**: Execute code cells as you read
4. **Complete mini-project**: Practice with the hands-on project
5. **Review summary**: Ensure you understood key concepts
6. **Monitor services**: Check Flink UI, Kafka logs

### Study Schedule Suggestions

**Intensive (1 week)**
- 1 module per day
- 1-1.5 hours per session
- Complete in 7 days

**Moderate (2-3 weeks)**
- 2-3 modules per week
- 1 hour per session
- Complete in 2-3 weeks

**Relaxed (4 weeks)**
- 1-2 modules per week
- 1 hour per session
- Complete in 4 weeks

## Technologies Used

### Core Streaming
- **Apache Kafka** - Distributed event streaming platform
- **Apache Flink** - Stream processing framework
- **Kafka Connect** - Data integration framework
- **Schema Registry** - Schema management for Kafka

### Python Libraries
- **confluent-kafka** - Kafka Python client
- **pyflink** - Python API for Apache Flink
- **avro-python3** - Avro serialization
- **kafka-python** - Alternative Kafka client

### Supporting Tools
- **Docker & Docker Compose** - Containerization
- **Jupyter** - Interactive development
- **pandas** - Data manipulation
- **matplotlib** - Visualization

### Monitoring
- **Kafka Manager** (optional) - Kafka cluster management
- **Flink Web UI** - Job monitoring
- **Prometheus** (optional) - Metrics collection

## Tips for Success

1. **Start Docker early**
   - Docker containers take time to start
   - Give them 1-2 minutes to fully initialize
   - Check logs if services don't start

2. **Monitor resource usage**
   - Kafka and Flink are resource-intensive
   - Close other applications if needed
   - Use `docker stats` to monitor containers

3. **Understand, don't memorize**
   - Focus on streaming concepts
   - Understand trade-offs (latency vs throughput)
   - Think about real-world applications

4. **Practice with variations**
   - Change windowing strategies
   - Try different partitioning keys
   - Experiment with parallelism

5. **Join the community**
   - Kafka Users Slack
   - Flink Forward community
   - Stack Overflow for troubleshooting

6. **Build incrementally**
   - Start simple, add complexity
   - Test each component separately
   - Use Flink/Kafka UIs for debugging

7. **Read error messages carefully**
   - Streaming errors can be cryptic
   - Check container logs
   - Verify network connectivity

## Troubleshooting

### Common Issues and Solutions

#### Issue: Docker containers won't start
```bash
# Solution: Clean up and restart
docker-compose down
docker-compose up -d

# Check for port conflicts
netstat -an | findstr "9092"  # Windows
lsof -i :9092  # Mac/Linux
```

#### Issue: Kafka connection refused
```bash
# Solution: Wait for Kafka to fully start
docker-compose logs kafka | tail -20

# Verify Kafka is running
docker-compose ps

# Restart just Kafka
docker-compose restart kafka
```

#### Issue: Flink job submission fails
```bash
# Solution: Check Flink UI (http://localhost:8081)
# Verify JobManager is running
docker-compose logs flink-jobmanager

# Check TaskManager slots
# Increase parallelism if needed in docker-compose.yml
```

#### Issue: Python package import errors
```bash
# Solution: Reinstall in correct environment
pip install --force-reinstall confluent-kafka pyflink

# Verify installation
python -c "import kafka; import pyflink; print('OK')"
```

#### Issue: Out of memory errors
```bash
# Solution: Increase Docker memory
# Docker Desktop -> Settings -> Resources -> Memory (8GB+)

# Or reduce container resources in docker-compose.yml
```

#### Issue: Notebooks can't connect to Kafka
```bash
# Solution: Use host.docker.internal on Windows/Mac
# Or localhost on Linux

# Verify connection
python scripts/setup_helpers.py --verify-kafka
```

### Getting Help

If you encounter issues not covered here:

1. **Check container logs**: `docker-compose logs [service-name]`
2. **Search Stack Overflow**: Tag with [apache-kafka] or [apache-flink]
3. **Review official documentation**: Kafka and Flink docs are excellent
4. **Ask in communities**: Kafka Users Slack, Flink Forward
5. **Create an issue**: If you find bugs in the notebooks, please report them

## Next Steps

After completing this course, consider these paths to deepen your streaming skills:

### Immediate Next Steps
1. **Build your own streaming project**
   - Choose a real-time use case
   - Implement end-to-end
   - Deploy locally or to cloud

2. **Explore cloud streaming**
   - AWS Kinesis + Flink on EMR
   - Google Cloud Dataflow
   - Azure Event Hubs + Stream Analytics

3. **Advanced Flink**
   - FlinkSQL and Table API
   - Complex Event Processing (CEP)
   - Machine Learning on streams

### Advanced Topics to Explore
- **Stream processing at scale**: Multi-datacenter Kafka, global deployments
- **Advanced CDC**: Full database replication, schema evolution
- **Stream ML**: Feature stores, online training
- **ksqlDB**: Stream processing with SQL
- **Kafka Streams**: Lightweight stream processing
- **Delta Lake/Iceberg**: Streaming to data lakes
- **Exactly-once semantics**: Deep dive into distributed transactions

### Recommended Resources
- **Books**:
  - "Kafka: The Definitive Guide" by Neha Narkhede et al.
  - "Streaming Systems" by Tyler Akidau et al.
  - "Designing Event-Driven Systems" by Ben Stopford

- **Online Courses**:
  - Confluent Developer Courses (free)
  - Flink Forward Training
  - Databricks Streaming Courses

- **Communities**:
  - Kafka Users Slack
  - Flink Forward
  - r/apachekafka (Reddit)

- **Practice**:
  - Confluent Cloud (free tier)
  - AWS Kinesis free tier
  - Build your own projects

## Contributing

This is a learning project, but improvements are welcome! If you find:
- Errors or typos in notebooks
- Better ways to explain concepts
- Additional streaming patterns
- Performance improvements

Please feel free to contribute or provide feedback.

## License

This project is part of a personal learning portfolio. Feel free to use it for your own learning purposes.

## Acknowledgments

This learning path was created to provide a structured, hands-on introduction to real-time stream processing. It draws from industry best practices, official documentation, and real-world streaming architectures.

Special thanks to the Apache Kafka and Apache Flink communities for creating these amazing open-source tools that power modern data platforms.

---

**Ready to start your streaming journey?**

Open `notebooks/00_setup_introduction.ipynb` and let's build real-time systems!

**Questions or feedback?** Create an issue or reach out through the portfolio repository.

Happy Streaming!
